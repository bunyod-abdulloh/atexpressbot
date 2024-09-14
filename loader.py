from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from data.config import BOT_TOKEN
from utils.db.postgres import Database

default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
db = Database()
bot = Bot(token=BOT_TOKEN, default=default_properties)
