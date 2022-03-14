# -*- coding: utf-8 -*-

from aiogram import types
from loader import dp
from keyboards import inline, ctypes
from statesgroup import CreateAd


@dp.message_handler(text="Продать собаку")
async def dog_sale(message: types.Message):
    await CreateAd.get_breed.set()
    await message.answer(
        text="Выберите породу собаки\n\n" + \
            "<em>Либо введите ее вручную:</em>",
        reply_markup=inline.dogs_breed()
    )


@dp.message_handler(text="Купить собаку")
async def dog_buy(message: types.Message):
    await message.answer(
        text="🐶 Перейдите в раздел для покупки собак",
        reply_markup=inline.buy_channel(),
    )
