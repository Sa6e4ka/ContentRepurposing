from aiogram.types import  Message, CallbackQuery
from .keybords import button
from Loggs import logger
import functools


'''
Декоратор для отлова ошибок
'''
def error_handler(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        message_or_call = next((arg for arg in args if isinstance(arg, (Message, CallbackQuery))), None)
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            username = (message_or_call.from_user.username 
                        if message_or_call and isinstance(message_or_call, (Message, CallbackQuery)) 
                        else 'Unknown user')
            logger.debug(f'У пользователя {username} возникла ошибка при выполнении функции "{func.__name__}": {e}')
            
            if message_or_call:
                error_message = "Кажется, что произошла ошибка 😨\n\nОбязательно напиши об этом @Megagigapoopfart"
                if isinstance(message_or_call, Message):
                    await message_or_call.answer(error_message, reply_markup=button(["Главное меню"]))
                elif isinstance(message_or_call, CallbackQuery):
                    await message_or_call.message.edit_text(error_message, reply_markup=button(["Главное меню"]))
    return wrapper