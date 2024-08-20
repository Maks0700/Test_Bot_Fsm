from .greeting import router as greeting_router
from .full_name import router as full_name_user
from .email_user import router as email_router
from .age_user import router as age_router
from aiogram import Router
router=Router(name=__name__)
router.include_routers(greeting_router,
                      full_name_user,
                      email_router,
                      age_router)






