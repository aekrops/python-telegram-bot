from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="python or java")
        ],
        [
            KeyboardButton(text="roll"),
            KeyboardButton(text="void")
        ]
    ],
    resize_keyboard=True
)
