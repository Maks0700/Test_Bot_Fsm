from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.filters import Command
from KEYBOARDS.common_keyboards import start_test_user
from ROUTERS.POLL.STATES import Meeting
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
 

router=Router(name=__name__)

@router.message(Meeting.age_user,F.text.isdigit())
async def process_age(message:Message,state:FSMContext):
    await state.update_data(age=message.text)
    data=await state.get_data()
    await message.answer(f"Good. Nice to meet you {data['full_name']}.",reply_markup=start_test_user())
    await state.clear()

@router.message(Meeting.age_user)
async def check_age(message:Message):
    await message.reply("Enter valide age!!")

