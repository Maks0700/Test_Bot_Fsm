from .polling import router as polling_router
from aiogram import Router

router=Router(name=__name__)

router.include_router(polling_router)