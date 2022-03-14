# -*- coding: utf-8 -*-

from aiogram import types


def get_media_group(album, content):
    media_group = types.MediaGroup()

    for i, obj in enumerate(album):
        if obj.photo:
            media = {
                "media": obj.photo[-1].file_id,
                "type": obj.content_type,
            }

            if i == 0:
                media["caption"] = content
            
            media_group.attach(media)
        
        if obj.video:
            media = {
                "media": obj.video.file_id,
                "type": obj.content_type,
            }

            if i == 0:
                media["caption"] = content
            
            media_group.attach(media)
    
    return media_group


def format_data_to_content(data):
    breed = data['breed']
    if breed == "gold":
        breed = "Голден ретривер/Золотой ретривет"

    return  "1️⃣ Breed / Порода\n" + \
            f"{breed}\n" + \
            "2️⃣Sex/Пол\n" + \
            f"{data['sex']}\n" + \
            "3️⃣Age/Возраст\n" + \
            f"{data['age']}\n" + \
            "4️⃣Prise/Цена\n" + \
            f"{data['price']} $\n" + \
            "5️⃣Pedigree/Родословная\n" + \
            f"{data['pedigree']}\n" + \
            "6️⃣Contact/Контакты\n" + \
            f"{data['phone']}\n\n" + \
            f"{data['comment']}"