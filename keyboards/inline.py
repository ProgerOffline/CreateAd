# -*- coding: utf-8 -*-

from data.config import BUY_CHANNEL_URL
from aiogram import types
from . import ctypes


def buy_channel():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Купить",
            url=BUY_CHANNEL_URL,
        )
    )


def dogs_breed():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Голден ретривер/Золотой ретривет",
            callback_data=ctypes.dog_breed.new(breed="gold")
        )
    ).add(
        types.InlineKeyboardButton(
            text="Лабрадор-ретривер",
            callback_data=ctypes.dog_breed.new(breed="Лабрадор-ретривер")
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Французский бульдог",
            callback_data=ctypes.dog_breed.new(breed="Французский бульдог")
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Хаски",
            callback_data=ctypes.dog_breed.new(breed="Хаски")
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Отменить ↩️",
            callback_data=ctypes.dog_breed.new(breed="cancel")
        )
    )


def dog_sex():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Кобель",
            callback_data=ctypes.dog_sex.new(sex="Кобель"),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Сука",
            callback_data=ctypes.dog_sex.new(sex="Сука"),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        )
    )


def dog_age():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            text="1 месяц",
            callback_data=ctypes.dog_age.new(age="1 месяц"),
        ),
        types.InlineKeyboardButton(
            text="4 месяца",
            callback_data=ctypes.dog_age.new(age="4 месяца"),
        ),
        types.InlineKeyboardButton(
            text="6 месяцев",
            callback_data=ctypes.dog_age.new(age="6 месяцев"),
        )
    ).row(
        types.InlineKeyboardButton(
            text="12 месяцев",
            callback_data=ctypes.dog_age.new(age="12 месяцев"),
        ),
        types.InlineKeyboardButton(
            text="24 месяца",
            callback_data=ctypes.dog_age.new(age="24 месяца"),
        ),
        types.InlineKeyboardButton(
            text="36 месяцев",
            callback_data=ctypes.dog_age.new(age="36 месяцев"),
        ),
    ).row(
        types.InlineKeyboardButton(
            text="48 месяцев",
            callback_data=ctypes.dog_age.new(age="48 месяцев"),
        ),
    ).row(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        )
    )


def get_price():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        )
    )


def get_pedigree():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="КСУ-FCI",
            callback_data=ctypes.dog_pedigree.new(pedigree="КСУ-FCI"),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="AKC",
            callback_data=ctypes.dog_pedigree.new(pedigree="AKC"),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        ),
    )


def get_phone():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        ),
    )

def get_comment():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Пропустить ➡️",
            callback_data=ctypes.skip.new(),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        ),
    )


def finish():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="Завершить 🔥",
            callback_data=ctypes.finish.new(type="finish"),
        )
    ).add(
        types.InlineKeyboardButton(
            text="Назад ↩️",
            callback_data=ctypes.back.new(),
        ),
    ).add(
        types.InlineKeyboardButton(
            text="Отменить ↩️",
            callback_data=ctypes.dog_breed.new(breed="cancel")
        )
    )


def confirm_upload():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="✅ Да",
            callback_data=ctypes.confirm.new(status="yes"),
        ),
        types.InlineKeyboardButton(
            text="❌ Нет",
            callback_data=ctypes.confirm.new(status="no"),
        )
    )