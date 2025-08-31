from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
from aiogram.types import CallbackQuery
env:Env = Env()
env.read_env()
disp = Dispatcher()

@disp.message(Command(commands="get_id"))
async def getId(callback_query : CallbackQuery):
    await callback_query.answer(f"{callback_query.from_user.id}")

async def main():
    BOT_TOKEN = env("BOT_TOKEN")
    bot = Bot(token = BOT_TOKEN, default= DefaultBotProperties(parse_mode= ParseMode.HTML))
    await disp.start_polling(bot)

asyncio.run(main())
   