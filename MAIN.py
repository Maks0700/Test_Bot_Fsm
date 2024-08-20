from aiogram import Dispatcher,Router,Bot
from aiogram.enums import ParseMode
from config import settings
import asyncio
from aiogram.exceptions import TelegramBadRequest
from ROUTERS import router as main_router

async def main():
    dp=Dispatcher()
    dp.include_routers(main_router)
    bot=Bot(
        token=settings.token,
        parse_mode=ParseMode.HTML
    )
    try:
        print("Suuccess")
        await dp.start_polling(bot)
    except TelegramBadRequest as t_b:
        print(t_b)
if __name__=="__main__":
    asyncio.run(main())

