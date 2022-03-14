# -*- coding: utf-8 -*-

from aiogram import executor
from loader import dp


async def on_startup(dp):
    import middlewares, handlers


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)