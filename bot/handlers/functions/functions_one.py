from aiogram.enums import ChatMemberStatus

from data.config import ADMINS
from loader import bot


async def check_channel_subscription(user_id: int, channel_id: int) -> bool:
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    if member.status == ChatMemberStatus.MEMBER or str(member.user.id) in ADMINS:
        return True
    else:
        return False


def extracter(all_medias, delimiter):
    empty_list = []
    for e in range(0, len(all_medias), delimiter):
        empty_list.append(all_medias[e:e + delimiter])
    return empty_list
