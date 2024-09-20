import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.middlewares.request_logging import logger

from bot.middlewares.mediagroup import MediaGroupMiddleware
from loader import db


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from bot.handlers import setup_routers

    dispatcher.include_router(setup_routers())


def setup_middlewares(dispatcher: Dispatcher) -> None:
    """MIDDLEWARE"""
    from bot.middlewares import ThrottlingMiddleware

    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))
    dispatcher.message.middleware(MediaGroupMiddleware())


def setup_filters(dispatcher: Dispatcher) -> None:
    """FILTERS"""
    from bot.filters import ChatPrivateFilter

    dispatcher.message.filter(ChatPrivateFilter(chat_type=["private"]))


async def setup_aiogram(dispatcher: Dispatcher) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher)
    setup_filters(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def database_connected():
    # Ma'lumotlar bazasini yaratamiz:
    await db.create()
    # await db.drop_table_users()
    await db.create_table_users()


async def on_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    from utils.set_bot_commands import set_default_commands
    from utils.notify_admins import on_startup_notify

    logger.info("Database connected")
    await database_connected()

    logger.info("Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    """CONFIG"""
    from data.config import BOT_TOKEN
    from aiogram.enums import ParseMode
    from aiogram.fsm.storage.memory import MemoryStorage
    default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=BOT_TOKEN, default=default_properties)
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)
    asyncio.run(dispatcher.start_polling(bot, close_bot_session=True,
                                         allowed_updates=dispatcher.resolve_used_update_types()))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot stopped!")
