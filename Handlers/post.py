from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter, or_f, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import  Message, CallbackQuery
 
from sqlalchemy.ext.asyncio import AsyncSession

import requests

# Start Router
post_router = Router()

@post_router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Привет!\n\nЭто бот для загрузки видео из Tik Tok на YouTube!\n\n<b>Отправь никнейм автора и его видео окажутся на канале</b>")

@post_router.message(F.text)
async def post(message: Message):
    try:
        url = "http://localhost:8000/post/"
        payload = {"author": message.text}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url=url, params=payload, headers=headers).json()
        for i in response:
            await message.answer(text=str(i["message"]))

    except Exception as e:
        await message.answer(f"Похоже, что возникла какая-то ошибка!\n\n<b>Обрабочик ошибки:</b>\n\n{e}")