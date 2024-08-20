from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.filters import Command
from ROUTERS.POLL.STATES import Meeting
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from VALIDATOR.valid_email import val_em
from aiogram.types import ReplyKeyboardRemove


router=Router(name=__name__)
@router.message(Meeting.email_user,F.text.cast(val_em).as_("email"))
async def process_email(message:Message,state:FSMContext,email:str):
    await state.update_data(email=email)
    text=f"Cool, your email: {markdown.hcode(email)}. Enter your age"
    await state.set_state(Meeting.age_user)
    await message.answer(text=text)
    

@router.message(Meeting.email_user)
async def check_email(message:Message):
    await message.reply(f"Your email {message.text} is not valid. Send me again!!")
    

