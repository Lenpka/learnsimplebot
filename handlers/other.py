import asyncio 
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

rout = Router()
@rout.message()
async def other(message:Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text = LEXICON_RU['no_echo'])