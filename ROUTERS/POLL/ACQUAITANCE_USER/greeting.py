from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.filters import Command
from ROUTERS.POLL.STATES import Meeting
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.fsm.state import any_state

router=Router(name=__name__)

@router.message(Command("survey",prefix="!/"))
async def start_poll(message:Message,state:FSMContext):
    text=markdown.hbold("Great, i am very glad to see you! Let's start to poll with our meeting. What is your name?")
    await message.answer(text=text)
    await state.set_state(Meeting.full_name_user)
    
    
    

@router.message(Command("cancel",prefix="!/"),Meeting())#Meeting need to pointed any state
@router.message(F.text.casefold()=="cancel",Meeting())
async def exit_test(message:Message,state:FSMContext):
    current_state=await state.get_state()
    if current_state is None:
        await message.answer("OK, if you wanna to start poll touch in /survey")
        return
    await message.answer("Wait to again in my poll.")
    await state.clear()
    await message.answer(f"Current state is {current_state}. Touch is /survey in order to start new poll!")
        
    
    
    
    

    
