from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


from loader import dp


async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}. I'm Mai Sakurajima")
