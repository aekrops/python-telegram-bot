from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from data import config
from handlers.users import start  # , menu, help
from aiogram.types import Message, File
from aiogram.dispatcher.filters import Command, CommandStart
from keyboards import menu
import random
import os
from data.download_video import upload_video_to_fb, get_path_of_video_from_fb


TOKEN = config.BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print("Bot started...")


@dp.message_handler(CommandStart())
async def starting(message: Message):
    await start.bot_start(message)


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Choose the option",  reply_markup=menu.menu)


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


@dp.message_handler(content_types=['video'])
async def read_video_from_user(message: Message):
    try:
        video_id = message.video.file_id
        video = await bot.get_file(video_id)
        video_path = video.file_path
        random_num = random.randint(0, 10000)
        await bot.download_file(video_path, f"amv{random_num}.mp4")
        upload_video_to_fb(f"amv{random_num}.mp4")
        os.remove(f"amv{random_num}.mp4")
        await bot.send_message(message.chat.id, "thanks for video :D")
        print("success")
    except:
        print("error")


@dp.message_handler(text="get amv")
async def read_video_from_dp(message: Message):
    try:
        await bot.send_video(message.chat.id, get_path_of_video_from_fb())
        print("success")
    except:
        print("error")

if __name__ == '__main__':
    from aiogram import executor
    # from handlers import dp
    executor.start_polling(dp)
