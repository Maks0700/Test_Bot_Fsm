from aiogram import Router
from .base_commands import router as base_commands_routers

router=Router(name=__name__)
router.include_router(
    base_commands_routers
)
