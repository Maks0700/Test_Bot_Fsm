from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.filters import Command
from ROUTERS.POLL.STATES import Meeting
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router=Router(name=__name__)
@router.message(Meeting.full_name_user,F.text)
async def name_proceess(message:Message,state:FSMContext):
    await state.set_state(Meeting.email_user)
    await message.answer("Super, send me please your valid email!")
    await state.update_data(full_name=message.text)

@router.message(Meeting.full_name_user,~F.text)
async def checking_name(message:Message):
    await message.answer("Send me valid name",quote=True)
    
    
    
    


