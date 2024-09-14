from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

select_language_dkb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="🇺🇿 O'zbek")
    ],
        [
            KeyboardButton(text="🇷🇺 Русский")
        ],
        [
            KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English")
        ]
    ],
    resize_keyboard=True
)


def main_dkb(texts):
    builder = ReplyKeyboardBuilder()
    for text in texts:
        builder.add(KeyboardButton(text=text))
    builder.adjust(1, 2, 1)
    return builder.as_markup(resize_keyboard=True)


def second_main_dkb(texts):
    builder = ReplyKeyboardBuilder()
    for text in texts:
        builder.add(KeyboardButton(text=text))
    builder.adjust(2, 2, 1, 1)
    return builder.as_markup(resize_keyboard=True)


def countries_dkb(texts):
    builder = ReplyKeyboardBuilder()
    for text in texts:
        builder.add(KeyboardButton(text=text))
    builder.adjust(2, 2, 2, 2, 1)
    return builder.as_markup(resize_keyboard=True)


def faq_dkb(texts):
    builder = ReplyKeyboardBuilder()
    for text in texts:
        builder.add(KeyboardButton(text=text))
    builder.adjust(1, 2, 1)
    return builder.as_markup(resize_keyboard=True)


def profile_dkb(texts):
    builder = ReplyKeyboardBuilder()
    for text in texts:
        builder.add(KeyboardButton(text=text))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
