# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import TypeOfFileMismatch
from data.config import CHANNEL_ID
from loader import dp, bot
from statesgroup import CreateAd
from keyboards import ctypes, inline
from utils import format_data_to_content


@dp.callback_query_handler(ctypes.dog_breed.filter(breed="cancel"), state="*")
async def cancel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.get_sex)
async def back_to_get_breed(call: types.CallbackQuery, state: FSMContext):
    await CreateAd.get_breed.set()
    await call.message.edit_text(
        text="Выберите породу собаки\n\n" + \
            "<em>Либо введите ее вручную:</em>",
        reply_markup=inline.dogs_breed()
    )


@dp.callback_query_handler(ctypes.dog_breed.filter(), state=CreateAd.get_breed)
@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.get_age)
async def save_breed(call: types.CallbackQuery,
        callback_data : dict, state: FSMContext):

    async with state.proxy() as data:
        data['breed'] = callback_data.get('breed')

    await CreateAd.next()
    await call.message.edit_text(
        text="2️⃣ <b>Пол собаки</b>",
        reply_markup=inline.dog_sex(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.dog_sex.filter(), state=CreateAd.get_sex)
@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.get_price)
async def get_sex(call: types.CallbackQuery, callback_data: dict,
        state: FSMContext):

    await CreateAd.get_age.set()
    async with state.proxy() as data:
        data['sex'] = callback_data.get('sex')

    await call.message.edit_text(
        text="3️⃣ <b>Выберите возраст</b>\n\n" +\
            "<em>Либо введите его вручную:</em>",
        reply_markup=inline.dog_age(),
    )

    await call.answer()


@dp.callback_query_handler(ctypes.dog_age.filter(), state=CreateAd.get_age)
@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.get_pedigree)
async def get_age(call: types.CallbackQuery, callback_data: dict,
        state: FSMContext):

    await CreateAd.get_price.set()
    async with state.proxy() as data:
        data['age'] = callback_data.get('age')
    
    await call.message.edit_text(
        text="4️⃣<b>Напишите цену в USD:</b>",
        reply_markup=inline.get_price(),
    )


@dp.callback_query_handler(ctypes.dog_pedigree.filter(), state=CreateAd.get_pedigree)
@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.get_comment)
async def get_pedigree(call: types.CallbackQuery, callback_data: dict,
        state: FSMContext):

    await CreateAd.get_phone.set()
    async with state.proxy() as data:
        data['pedigree'] = callback_data.get('pedigree')

    await call.message.edit_text(
        text="6️⃣ <b>Напишите свой номер в международном формате:</b>",
        reply_markup=inline.get_phone(),
    )
    await call.answer()


@dp.callback_query_handler(ctypes.skip.filter(), state=CreateAd.get_comment)
async def skip_comment(call: types.CallbackQuery, state: FSMContext):
    await CreateAd.finish.set()
    async with state.proxy() as data:
        data['comment'] = ""


    await call.message.edit_text(
        text="<em>Теперь отправьте одно или несколько фото " +\
            "и\или видео либо нажмите</em> <b>ЗАВЕРШИТЬ 🔥!</b>",
        reply_markup=inline.finish()
    )


@dp.callback_query_handler(ctypes.back.filter(), state=CreateAd.finish)
async def back_to_get_comment(call: types.CallbackQuery, state: FSMContext):
    await CreateAd.get_comment.set()
    await call.message.edit_text(
        text="7️⃣ <b>Напишите ваш комментарий:</b>",
        reply_markup=inline.get_comment(),
    )


@dp.callback_query_handler(ctypes.finish.filter(), state=CreateAd.finish)
async def finish(call: types.CallbackQuery, callback_data: dict,
        state: FSMContext):
    
    async with state.proxy() as data:
        data['media'] = ""
        content = format_data_to_content(data)

    await call.message.answer(text="<b>Закончили заполнять Объявления!</b>")
    await call.message.answer(text=content)
    await call.message.answer(
        text="<b>Внимательно проверьте текст Объявления выше!</b>" + \
            "<b>Внимание!</b> Пост ещё не отправлен на проверку." + \
            "<em>Подтвердите публикацию, либо отмените.</em>",
        reply_markup=inline.confirm_upload()
    )


@dp.callback_query_handler(ctypes.confirm.filter(), state=CreateAd.finish)
async def upload(call: types.CallbackQuery, callback_data: dict,
        state: FSMContext):

    if callback_data['status'] == "no":
        await call.message.edit_text(
            text="<b>Создание Объявления отменено!</b>\n\n" + \
            "Спасибо, что воспользовались нашей площадкой!"
        )
        await state.finish()
        return


    async with state.proxy() as data:
        content = format_data_to_content(data)
        media = data['media']
    
    if isinstance(media, types.MediaGroup):
        await bot.send_media_group(
            chat_id=CHANNEL_ID,
            media=media,
        )
        await state.finish()
        await call.message.edit_text(
            text="<b>Объявления ,было отправлено!</b>\n\n" + \
            "Спасибо, что воспользовались нашей площадкой!"
        )
        return
    
    if media == "":
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=content,
        )
        await state.finish()
        await call.message.edit_text(
            text="<b>Объявления ,было отправлено!</b>\n\n" + \
            "Спасибо, что воспользовались нашей площадкой!"
        )
        return
    
    try:
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=media,
            caption=content,
        )
    except TypeOfFileMismatch:
        await bot.send_video(
            chat_id=CHANNEL_ID,
            video=media,
            caption=content
        )

    await call.message.edit_text(
        text="<b>Объявления ,было отправлено!</b>\n\n" + \
        "Спасибо, что воспользовались нашей площадкой!"
    )
    await state.finish()