# -*- coding: utf-8 -*-

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
BUY_CHANNEL_URL = "https://t.me/worldwidepuppies"
CHANNEL_ID = 535327818