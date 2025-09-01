import logging
import asyncio
from config.config import Config, load_config
from handlers import other, user

from aiogram.filters import Command
from aiogram import Bot, Dispatcher

async def main() -> None:
    config: Config = load_config()
    logging.basicConfig(
        level= logging.getLevelName(level = config.log.level),
        format = config.log.format,
    )
    bot = Bot(token = config.bot.token)
    disp = Dispatcher()
    #Инициализация хэнддеров (роутеров) в диспетчере
    disp.include_router(user.rout)
    disp.include_router(other.rout)

    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot)

asyncio.run(main())