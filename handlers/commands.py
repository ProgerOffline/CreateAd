# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp
from keyboards import reply


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        text="<b>Добро пожаловать, ProgerOffline!</b>\n\n" +\
            "💠Элитные собаки на продажу со всего мира 🌐\n" +\
            "❗️Только у нас в канале❗️\n" +\
            "@worldwidepuppies\n\n" +\
            "🐶 Покупка - Продажа собак 🐕\n" +\
            "✅Бесплатно через нашего бота.\n" +\
            "@animalsellerbot\n\n"+\
            "🗽Доставка собак по всему миру. 🛩\n" +\
            "@tatdovmat\n\n" +\
            "🏆Группа для обсуждения питомцев\n" +\
            "@worldwideanimals\n\n" +\
            "🇬🇧\n" +\
            "💠Elite dogs for sale from all over the world 🌐\n" +\
            "❗️Only in our channel❗️\n" +\
            "@worldwidepuppies\n\n" +\
            "🐶 Buying - Selling Dogs 🐕\n" +\
            "✅Unlessly through our bot.\n" +\
            "@animalsellerbot\n\n" +\
            "🗽Dog delivery worldwide. 🛩\n" +\
            "@tatdovmat\n\n" +\
            "🏆Pet Discussion Group\n" +\
            "@worldwideanimals",
        reply_markup=reply.start()
    )