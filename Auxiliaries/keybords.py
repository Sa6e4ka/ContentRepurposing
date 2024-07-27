from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

'''
Клавиатура главного меню
'''
StartKB = InlineKeyboardBuilder()
buttons_list = ["Добавить слово в свой словарь", "Учить свои слова", "Учить по темам", "Добавить слова по темам", "Рейтинговая игра"]

for i in buttons_list:
    StartKB.button(text=i, callback_data=i)
StartKB.adjust(1, 2, 1, 1, 1)


'''
Функция для созданяи inline-клавиатуры
'''
def button(text : list):
    KB = InlineKeyboardBuilder()
    for i in text:
        KB.button(text=i, callback_data=i)
    KB.adjust(1,)
    return KB.as_markup()

