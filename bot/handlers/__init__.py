from aiogram import Router

from bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start_hr
    from .uz import (main_hr, id_hr, packages_hr, calc_hr, profile_hr, manual_hr, tracking_hr, faq_hr, call_to_admin_hr,
                     tarifs_hr)
    from .errors import error_handler
    from .admin import admin_main, admin_users, admin_downloads, admin_check

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    main_hr.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    #  Users
    router.include_routers(start_hr.router, main_hr.router, id_hr.router, packages_hr.router, calc_hr.router,
                           profile_hr.router, manual_hr.router, tracking_hr.router, faq_hr.router,
                           call_to_admin_hr.router, tarifs_hr.router)
    # Admins
    router.include_routers(admin_main.router, admin_users.router, admin_downloads.router, admin_check.router)
    return router
