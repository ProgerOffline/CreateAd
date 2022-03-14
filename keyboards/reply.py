# -*- coding: utf-8 -*-

from aiogram import types


def start():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1
    ).row(
        types.KeyboardButton("Продать собаку"),
        types.KeyboardButton("Купить собаку")
    )