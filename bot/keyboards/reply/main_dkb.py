from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


uzmain_start_dkb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📦 Yukni tekshirish")
    ],
        [
            KeyboardButton(text="🆔 ID olish"),
            KeyboardButton(text="🧮 Hisoblar")
        ],
        [
            KeyboardButton(text="💸 Yuan xarid qilish")
        ],
        [
            KeyboardButton(text="📲 Aloqa"),
            KeyboardButton(text="🧑‍💻 Bot yo'riqnomasi")
        ],
        [
            KeyboardButton(text="🇨🇳  Onlayn savdo platformalari")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Habaringizni kiriting...",
    one_time_keyboard=True
)

uzmain_dkb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📦 Yukni tekshirish")
    ],
        [
            KeyboardButton(text="📍 Manzil olish"),
            KeyboardButton(text="🧮 Hisoblar")
        ],
        [
            KeyboardButton(text="💸 Yuan xarid qilish")
        ],
        [
            KeyboardButton(text="📲 Aloqa"),
            KeyboardButton(text="🧑‍💻 Bot yo'riqnomasi")
        ],
        [
            KeyboardButton(text="🇨🇳  Onlayn savdo platformalari")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Habaringizni kiriting...",
    one_time_keyboard=True
)
