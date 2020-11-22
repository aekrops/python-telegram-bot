from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        "Commands:",
        "/start - start conversation",
        "/help - info",
        "/roll - get random number in range 0-100"
    ]
    await message.answer('\n'.join(text))
