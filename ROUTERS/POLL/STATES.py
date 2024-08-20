from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from enum import Enum

class Meeting(StatesGroup):
    full_name_user=State()
    email_user=State()
    age_user=State()
    

class Poll(StatesGroup):
    war_question=State()
    baptism_of_rus=State()
    nobel_prize=State()

class Questions(str,Enum):
    answer_war="В каком году началась Отечественная Война?"
    baptism_rus="В каком году было крещение Руси?"
    nobel_prize_answer="Кто получил Нобелевскую премию за теорию относительности?"

class Topic_Test(str,Enum):
    WAR_TOPIC="Patriotic War"
    BAPTISM="Baptism of Russia"
    PHYSIC="Relativity Theory"
    
      

    
