import logging
import asyncio
from config.config import Config, load_config
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

    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot)

asyncio.run(main())