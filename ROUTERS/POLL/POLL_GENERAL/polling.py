from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.filters import Command
from ROUTERS.POLL.STATES import Questions, Meeting, Poll, Topic_Test
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from KEYBOARDS.common_keyboards import keyboard_next
from aiogram.types import CallbackQuery,ReplyKeyboardRemove

router=Router(name=__name__)



##Logica
first_quest=["1812","1921","1834"]
second_quest=["1002","892","988"]
third_quest=["Нильс Бор","Альберт Энштейн","Никола Тесла"]
right_answer=("1812","988","Альберт Энштейн")
@router.message(F.text=="Начать тестирование.")
async def start_test(message:Message,state:FSMContext):
    await state.set_state(Poll.war_question)
    await message.answer(text=Questions.answer_war,reply_markup=keyboard_next(first_quest))



    



@router.message(Command("cancel"),Poll())
@router.message(F.text.casefold=="cancel",Poll())
async def check_message(message:Message,state:FSMContext):
    current_state=await state.get_state()
    if current_state is None:
        await message.reply("Вы вышли из теста,если желаете снова начать нажмите /survey",reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(f"У вас текущее состояние {current_state}. Если хотите начать заново нажмите /survey",reply_markup=ReplyKeyboardRemove())
    await state.clear()



@router.message(Poll.war_question,F.text.in_(first_quest))
async def first_q(message:Message,state:FSMContext):
    await state.update_data(answ1=message.text)
    await state.set_state(Poll.baptism_of_rus)
    await message.answer(text=Questions.baptism_rus,reply_markup=keyboard_next(second_quest))

@router.message(Poll.war_question)
async def start_test(message:Message,state:FSMContext):
    await message.reply("Пользуйтесь только встроеннными кнопками!!")
    
@router.message(Poll.baptism_of_rus,F.text.in_(second_quest))
async def sec_q(message:Message,state:FSMContext):
    await state.update_data(answ2=message.text)
    await state.set_state(Poll.nobel_prize)
    await message.answer(text=Questions.nobel_prize_answer,reply_markup=keyboard_next(third_quest))
    
@router.message(Poll.baptism_of_rus)
async def first_q(message:Message,state:FSMContext):
    await message.reply("Пользуйтесь только встроеннными кнопками!!")

    
@router.message(Poll.nobel_prize,F.text.in_(third_quest))
async def third_q(message:Message,state:FSMContext):
    
    count_right=0
    await state.update_data(answ3=message.text)
    data=await state.get_data()
    await state.clear()
    
    result=[]
    [
        result.append(value)
        for value in data.values()
    ]
    for i in range(len(right_answer)):
        if result[i]==right_answer[i]:
            count_right+=1
    
    if count_right>=2:
        await message.answer(f"Молодец ты круто справился с задачей и ответил правильно на {count_right}",reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Позорный двоечник!!Иди учи историю!",reply_markup=ReplyKeyboardRemove())


@router.message(Poll.nobel_prize)
async def first_q(message:Message,state:FSMContext):
    await message.reply("Пользуйтесь только встроеннными кнопками!!")





        
         
