# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateAd(StatesGroup):
    get_breed = State()
    get_sex = State()
    get_age = State()
    get_price = State()
    get_pedigree = State()
    get_phone = State()
    get_comment = State()
    get_media = State()
    finish = State()