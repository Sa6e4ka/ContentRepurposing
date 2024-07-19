import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

prompt_list = [
  "you're a prompted generative model created tp generate titles for meme videos on youtube shorts. \nYour main task is to make different titles every time. Use all your dataset to it.",
  "input: make a title for a meme video",
  "output: Memes You Can't Miss #meme #funny #viral #lmao",
  "input: create a new title for meme video",
  "output: Internet's Funniest Memes #hilarious #viral #lol #meme",
  "input: i have a meme video. Create a title to it!",
  "output: Top Memes of the Week  #meme #funny #trending #viral",
  "input: Please make a hillarious title to my new video!",
  "output: Laugh Out Loud Memes  #funny #viral #memes #comedy",
  "input: A title to meme video, please",
  "output: Daily Dose of Memes  #meme #funny #viral #lol",
  "input: i would like to ask you ti make me a title to meme video on youtube shorts",
  "output: Best Internet Memes #hilarious #meme #viral #laugh",
  "input: make a title to new meme video pls!",
  "output: Must-See Memes #meme #funny #viral #memes",
  "input: Make a title to meme video!",
  "output: ",
]


def generate(credentials) -> str:
    '''
    Модель для генерации названий к видео (дообученная)
    '''
    genai.configure(credentials=credentials)

    generation_config = {
        "temperature": 1,
        "top_p": 1,
        "max_output_tokens": 500,
        "response_mime_type": "text/plain"
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config
    )

    response = model.generate_content(contents=prompt_list)


    return str(response.text)
