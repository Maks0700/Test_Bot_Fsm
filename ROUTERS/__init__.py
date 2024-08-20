from aiogram import Router
from .commands import router as command_router
from .POLL.ACQUAITANCE_USER import router as acquatince_router
from .POLL.POLL_GENERAL import router as gen_poll_router
router=Router(name=__name__)
router.include_routers(acquatince_router,
                    
                       gen_poll_router,
                       command_router)
