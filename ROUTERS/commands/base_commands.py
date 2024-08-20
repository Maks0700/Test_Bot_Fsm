from aiogram.types import Message
from aiogram import F,Router
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from aiogram.filters import CommandStart,Command
from KEYBOARDS.common_keyboards import get_start_keyboard,Buttons_help
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from ROUTERS.POLL.STATES import Meeting
router=Router(name=__name__)

@router.message(CommandStart())
async def greeting(message:Message):
    await message.answer(f"Welcome {markdown.hbold(message.from_user.first_name)} to my bot. If you gonna to start in my poll tap please /survey",parse_mode=ParseMode.HTML
                        )



@router.message(Command("help", prefix="!/"))
async def handle_help(message:Message):
    text=markdown.text(
        markdown.markdown_decoration.quote("I am an {echo} bot"),
        markdown.text(
            "Send me",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("iterally"),
                    "any",
                ),
            ),
            markdown.markdown_decoration.quote("message!"),
            
        ),
        sep="\n",
    )
    await message.answer(text=text,parse_mode=ParseMode.MARKDOWN_V2,reply_markup=ReplyKeyboardRemove())



@router.message(Command("describe", prefix="!/"))
async def handle_help(message:Message):
    text=markdown.text(f"In this bot, my dear {markdown.hcode(message.from_user.first_name)}, you get to know yourself inside!!!")
    await message.answer(text=text)
    


@router.message(Command("cancel"))
@router.message(F.text.casefold()=="cancel")
async def exit_test(message:Message):
    await message.answer("OK, goodbye.")
    
   


@router.message(F.text)
async def reply_to_user(message:Message):
    await message.reply(f"If you don't know that reply, me send to you list of button help",reply_markup=get_start_keyboard())
    