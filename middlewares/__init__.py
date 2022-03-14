# -*- coding: utf-8 -*-

from loader import dp
from .logger_middleware import UpdateLoggerMiddleware
from .album_middleware import AlbumMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())
    dp.middleware.setup(AlbumMiddleware())