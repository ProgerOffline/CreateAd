# -*- coding: utf-8 -*-

from aiogram.utils.callback_data import CallbackData

from keyboards.inline import finish


dog_breed = CallbackData("dog_breed", "breed")
dog_sex = CallbackData("dog_sex", "sex")
dog_age = CallbackData("dog_age", "age")
dog_pedigree = CallbackData("dog_pedigree", "pedigree")
finish = CallbackData("finish", "type")

back = CallbackData("back")
skip = CallbackData("skip")
confirm = CallbackData("confirm", "status")