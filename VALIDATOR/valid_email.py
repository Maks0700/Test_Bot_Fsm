from typing import Iterable
from email_validator import validate_email,EmailNotValidError
from aiogram.types import Message

first_quest=["1812","1921","1834"]
second_quest=["1002","892","988"]
third_quest=["Нильс Бор","Альберт Энштейн","Никола Тесла"]


def val_em(text:str)->str:
    
    try:
        email=validate_email(text)
    except EmailNotValidError:
        return None
    return email.normalized



    
        
    