from lexicon.lexicon import LEXICON_RU
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

@disp.message(CommandStart())
async def start(message:Message):
    await message.answer(text = LEXICON_RU['/start'])

@disp.message(command = Command(commands='/help'))
async def help(message:Message):
    await message.answer(text = LEXICON_RU['/help'])
