from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_id_ikeys():
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Ha", callback_data="get_iduz_yes")
            ],
            [
                InlineKeyboardButton(text="❌ Yo'q", callback_data="get_iduz_no")
            ]
        ]
    )
    return button


uz_users_payment_ikb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="Yuklar tarixi", callback_data=f"uz_cargo_history"
        ),
        InlineKeyboardButton(text="To'lovlar tarixi", callback_data=f"uz_payment_history")
    ],
        [
            InlineKeyboardButton(
                text="To'lov qilish", callback_data="pay_uz"
            )
        ]]
)


def courses_ibuttons(items, current_page, all_pages):
    keys = InlineKeyboardBuilder()
    for item in items:
        keys.add(
            InlineKeyboardButton(
                text=f"{item['table_number']}",
                callback_data=f"courses:{item['table_number']}:{current_page}"
            )
        )
    keys.adjust(5)
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"courses_prev:{current_page}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"courses_alert:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"courses_next:{current_page}"
        )
    )
    return keys.as_markup()


def key_returner_selected(items, table_name, current_page, all_pages, selected):
    keys = InlineKeyboardBuilder()
    for item in items:
        if selected == item['lesson_number']:
            keys.add(
                InlineKeyboardButton(
                    text=f"[ {item['lesson_number']} ]",
                    callback_data=f"id:{item['lesson_number']}:{current_page}:{table_name}"
                )
            )
        else:
            keys.add(
                InlineKeyboardButton(
                    text=f"{item['lesson_number']}",
                    callback_data=f"id:{item['lesson_number']}:{current_page}:{table_name}"
                )
            )
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev:{current_page}:{table_name}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertmessage:{current_page}:{table_name}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next:{current_page}:{table_name}"
        )
    )
    return keys.as_markup()


def key_returner_articles(current_page, all_pages):
    keys = InlineKeyboardBuilder()
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev_articles:{current_page}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertarticles:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next_articles:{current_page}"
        )
    )
    return keys.as_markup()


def key_returner_projects(items, current_page, all_pages):
    keys = InlineKeyboardBuilder()
    for item in items:
        keys.add(
            InlineKeyboardButton(
                text=f"{item['rank']}",
                callback_data=f"projects:{item['id']}"
            )
        )
    keys.adjust(5)
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev_projects:{current_page}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alert_projects:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next_projects:{current_page}"
        )
    )
    return keys.as_markup()


def interviews_first_ibuttons(items, current_page, all_pages, selected):
    builder = InlineKeyboardBuilder()
    for item in items:
        if selected == item['sequence']:
            builder.add(
                InlineKeyboardButton(
                    text=f"[ {item['sequence']} ]",
                    callback_data=f"select_projects:{item['id']}:{current_page}"
                )
            )
        else:
            builder.add(
                InlineKeyboardButton(
                    text=f"{item['sequence']}",
                    callback_data=f"select_pts:{item['id']}:{current_page}"
                )
            )
    builder.adjust(5)
    builder.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev_pts:{current_page}:{items[0]['id']}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alert_pts:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next_pts:{current_page}:{items[0]['id']}"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="📖 Mundarija",
            callback_data=f"content_projects:{current_page}:{items[0]['category']}"
        )
    )
    return builder.as_markup()

# async def tables_menu(callback_text):
#     all_tables = await db.select_all_tables()
#
#     builder = keyboard.InlineKeyboardBuilder()
#
#     for table in all_tables:
#         builder.add(
#             InlineKeyboardButton(
#                 text=f"{table['table_name']}", callback_data=f"{callback_text}_{table['id']}"
#             )
#         )
#     builder.adjust(1)
#     return builder.as_markup()
