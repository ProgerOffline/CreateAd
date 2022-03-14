# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from statesgroup import CreateAd
from keyboards import inline
from typing import List
from utils import format_data_to_content, get_media_group


@dp.message_handler(state=CreateAd.get_breed)
async def get_breed(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['breed'] = message.text

        await CreateAd.next()
        await message.answer(
            text="2️⃣ <b>Пол собаки</b>",
            reply_markup=inline.dog_sex(),
        )


@dp.message_handler(state=CreateAd.get_age)
async def get_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

        await CreateAd.get_price.set()
        await message.answer(
            text="4️⃣<b>Напишите цену в USD:</b>",
            reply_markup=inline.get_price(),
        )

@dp.message_handler(state=CreateAd.get_pedigree)
async def get_pedigree(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pedigree'] = message.text

        await CreateAd.get_phone.set()
        await message.answer(
            text="6️⃣ <b>Напишите свой номер в международном формате:</b>",
            reply_markup=inline.get_phone(),
        )


@dp.message_handler(state=CreateAd.get_price)
async def get_price(message: types.Message, state: FSMContext):
    try:
        price = int(message.text)
    except ValueError:
        await message.answer(
            text="⛔️ Пожалуйста, введите корректную сумму!" +\
            " Вы указали не число либо меньше 0!",
        )
        return
    
    if price <= 0:
        await message.answer(
            text="⛔️ Пожалуйста, введите корректную сумму!" +\
            " Вы указали не число либо меньше 0!",
        )
        return

    await CreateAd.get_pedigree.set()
    async with state.proxy() as data:
        data['price'] = price
    
    await message.answer(
        text="5️⃣ <b>Выберете родословную:</b>\n\n" + \
            "<em>Либо введите его вручную:</em>",
        reply_markup=inline.get_pedigree(),
    )


@dp.message_handler(state=CreateAd.get_phone)
async def get_phone(message: types.Message, state: FSMContext):
    await CreateAd.get_comment.set()
    async with state.proxy() as data:
        data['phone'] = message.text
    
    await message.answer(
        text="7️⃣ <b>Напишите ваш комментарий:</b>",
        reply_markup=inline.get_comment(),
    )


@dp.message_handler(state=CreateAd.get_comment)
async def get_comment(message: types.Message, state: FSMContext):
    await CreateAd.finish.set()
    async with state.proxy() as data:
        data['comment'] = message.text
    
    await message.answer(
        text="<em>Теперь отправьте одно или несколько фото " +\
            "и\или видео либо нажмите</em> <b>ЗАВЕРШИТЬ 🔥!</b>",
        reply_markup=inline.finish()
    )


@dp.message_handler(
    is_media_group=True, 
    content_types=types.ContentType.ANY,
    state=CreateAd.finish
)
async def handle_albums(message: types.Message, album: List[types.Message],
        state: FSMContext):
    async with state.proxy() as data:
        content = format_data_to_content(data)
        media_group = get_media_group(album, content)

        data['media'] = media_group

    await message.answer_media_group(media_group)


@dp.message_handler(content_types=['photo', 'video'], state=CreateAd.finish)
async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        content = format_data_to_content(data)
    
        await message.answer(text="<b>Закончили заполнять Объявления!</b>")
        if message.photo:
            data['media'] = message.photo[-1].file_id
            await message.answer_photo(
                photo=message.photo[-1].file_id,
                caption=content,
            )
        
        if message.video:
            data['media'] = message.video.file_id
            await message.answer_video(
                video=message.video.file_id,
                caption=content,
            )
    
    await message.answer(
        text="<b>Внимательно проверьте текст Объявления выше!</b>" + \
            "<b>Внимание!</b> Пост ещё не отправлен на проверку." + \
            "<em>Подтвердите публикацию, либо отмените.</em>",
        reply_markup=inline.confirm_upload()
    )