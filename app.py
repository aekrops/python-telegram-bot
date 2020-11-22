from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import data.config as config
from handlers.users import start # , menu, help
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, CommandStart
from keyboards import menu
import random

TOKEN = config.BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print("Bot started...")


@dp.message_handler(CommandStart())
async def starting(message: Message):
    await start.bot_start(message)


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Choose the option", reply_markup=menu.menu)


@dp.message_handler(text="roll")
async def roll(message: Message):
    print(message.from_user.id)
    print(message.chat.id)
    number = random.randint(0, 100)
    await bot.send_message(message.chat.id, str(number))


@dp.message_handler(text="python or java")
async def wise_choice(message: Message):
    languages = ["Java", "Python"]
    answer = languages[random.randint(0, 1)]
    await bot.send_message(message.chat.id, answer)


@dp.message_handler(text="void")
async def void_f(message: Message):
    pass


if __name__ == '__main__':
    from aiogram import executor
    # from handlers import dp
    executor.start_polling(dp)
