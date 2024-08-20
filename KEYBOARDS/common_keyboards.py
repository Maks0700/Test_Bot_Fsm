from typing import Iterable
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton,KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder









class Buttons_help:
    help="/help"
    describe="/describe"


def get_start_keyboard()->ReplyKeyboardMarkup:
    button_help = KeyboardButton(text=Buttons_help.help)
    button_desc = KeyboardButton(text=Buttons_help.describe)

    buttons_first_row = [button_help, button_desc]

    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row],
        resize_keyboard=True
        )
    return markup




def start_test_user():
    
    
    keyboard=ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Начать тестирование.")]
                  ],
        resize_keyboard=True
    )
    return keyboard

    



def keyboard_next(options:list):
    builder=ReplyKeyboardBuilder()
    for option in options:
        builder.button(text=option)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
    


    