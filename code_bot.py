from loguru import logger
import configparser
import gc
from memory_profiler import profile

import telebot
from telebot import types
from telebot.types import InputMediaPhoto, InputMediaVideo

from PIL import Image, ImageDraw, ImageFont

import time
from time import strftime,gmtime
from datetime import datetime, timedelta

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles import STYLE_MAP
from pygments.style import Style
from pygments.token import Token
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace

import os
import io

from array import array

import random

logger.add("file_1.log", rotation="500 MB")

# Обявляем парсер и задаем конфигурационный фаил
config = configparser.ConfigParser()  
config.read("settings.ini")

# берем токен бота из конфигурационного файла
bot = telebot.TeleBot(config["Telegramm"]["bot_token"])

# Оформление стили синтаксиса кода
class MyStyle(Style):
    background_color = "#191919"
    default_style = ""

    styles = {
        Comment: "#6272a4",
        Comment.Hashbang: "#6272a4",
        Comment.Multiline: "#6272a4",
        Comment.Preproc: "#ff79c6",
        Comment.Single: "#6272a4",
        Comment.Special: "#6272a4",

        Generic: "#f8f8f2",
        Generic.Deleted: "#8b080b",
        Generic.Emph: "#f8f8f2 underline",
        Generic.Error: "#f8f8f2",
        Generic.Heading: "#f8f8f2 bold",
        Generic.Inserted: "#f8f8f2 bold",
        Generic.Output: "#44475a",
        Generic.Prompt: "#f8f8f2",
        Generic.Strong: "#f8f8f2",
        Generic.Subheading: "#f8f8f2 bold",
        Generic.Traceback: "#f8f8f2",

        Error: "#f8f8f2",

        Keyword: "#ff79c6",
        Keyword.Constant: "#ff79c6",
        Keyword.Declaration: "#8be9fd italic",
        Keyword.Namespace: "#ff79c6",
        Keyword.Pseudo: "#ff79c6",
        Keyword.Reserved: "#ff79c6",
        Keyword.Type: "#8be9fd",

        Literal: "#f8f8f2",
        Literal.Date: "#f8f8f2",

        Name: "#f8f8f2",
        Name.Attribute: "#50fa7b",
        Name.Builtin: "#8be9fd italic",
        Name.Builtin.Pseudo: "#f8f8f2",
        Name.Class: "#50fa7b",
        Name.Constant: "#f8f8f2",
        Name.Decorator: "#f8f8f2",
        Name.Entity: "#f8f8f2",
        Name.Exception: "#f8f8f2",
        Name.Function: "#50fa7b",
        Name.Label: "#8be9fd italic",
        Name.Namespace: "#f8f8f2",
        Name.Other: "#f8f8f2",
        Name.Tag: "#ff79c6",
        Name.Variable: "#8be9fd italic",
        Name.Variable.Class: "#8be9fd italic",
        Name.Variable.Global: "#8be9fd italic",
        Name.Variable.Instance: "#8be9fd italic",

        Number: "#bd93f9",
        Number.Bin: "#bd93f9",
        Number.Float: "#bd93f9",
        Number.Hex: "#bd93f9",
        Number.Integer: "#bd93f9",
        Number.Integer.Long: "#bd93f9",
        Number.Oct: "#bd93f9",

        Operator: "#ff79c6",
        Operator.Word: "#ff79c6",

        Other: "#f8f8f2",

        Punctuation: "#f8f8f2",

        String: "#f1fa8c",
        String.Backtick: "#f1fa8c",
        String.Char: "#f1fa8c",
        String.Doc: "#f1fa8c",
        String.Double: "#f1fa8c",
        String.Escape: "#f1fa8c",
        String.Heredoc: "#f1fa8c",
        String.Interpol: "#f1fa8c",
        String.Other: "#f1fa8c",
        String.Regex: "#f1fa8c",
        String.Single: "#f1fa8c",
        String.Symbol: "#f1fa8c",

        Text: "#f8f8f2",

        Whitespace: "#f8f8f2"

    }

# Оформляем код в картинку и сохраняем припомощи модуля Pygments
def code2img(string):
    python_code = string
    png_code = highlight(python_code, PythonLexer(), ImageFormatter(
        font_size=20,
        style=MyStyle,
        line_number_bg='#191919',
        line_number_fg = '#697187',
        line_number_separator=False
        ))

    image = Image.open(io.BytesIO(png_code))
    image.save('code2img2.jpg')

# Собираем красивую картинку и отправляем ее
def CollectImage(string,id_chat): 
    code2img(string)
    text = string

    logger.info('Получили код от'+str(id_chat))

    long_line = 0
    line_width = 0
    text = text+'\n'

    #создаем картинку с кодом и сохраняем ее
    image_code = Image.open("code2img2.jpg").convert("RGBA")

    height = 150+image_code.size[1]
    width = 150+image_code.size[0]

    # создаем картинку
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    img = Image.new('RGB', (width+50, height), color = (r,g,b))
    d = ImageDraw.Draw(img)
    
    # Шапка
    d.ellipse([(50,30),(80,60)], fill=(25,25,25,128))
    d.ellipse([(width-30,30),(width,60)], fill=(25,25,25,128))
    d.rectangle([(70, 30) , (width-10,80)], fill=(25,25,25,128))

    # Заливка всего поля
    d.rectangle([(50, 50) , (width,height-50)], fill=(25,25,25,128))

    # Кноки закрыть, свернуть, на всеь экран
    d.ellipse([(70,50),(90,70)], fill=(200,20,20,128))
    d.ellipse([(100,50),(120,70)], fill=(253,233,16,128))
    d.ellipse([(130,50),(150,70)], fill=(0,255,0,128))

    # футер    
    d.ellipse([(50,height-60),(80,height-30)], fill=(25,25,25,128))
    d.ellipse([(width-30,height-60),(width,height-30)], fill=(25,25,25,128))
    d.rectangle([(70, height-30) , (width-20,height-80)], fill=(25,25,25,128))

    # картинка с кодом
    img.paste(image_code, (50,80),image_code)

    # Обрезаем лишнее
    cropimg = img.crop((0,0,width+50,height))
    
    # сохраняем для отправки
    cropimg.save('pil_text_font.png')

    # Отправляем картинку с кодом
    imgOut = open('pil_text_font.png','rb')
    bot.send_photo(id_chat, imgOut, caption='картинка сделанна ботом')
    imgOut.close()

    logger.info('отправили картинку кода в '+str(id_chat))

# Реагируем на /code
@bot.message_handler(commands=['code'])
def ParsToCode(message):
    logger.info('получили код от '+str(message.chat.id))
    CollectImage(message.text[6:],message.chat.id)

# пишем код в боте
@bot.message_handler(content_types=['text'])
def GetTextMessages(message):
    text = message.text
    id_chat = message.from_user.id
    CollectImage(text,id_chat)

# Установка соединения
def Connect():
    try:
        bot.polling( none_stop = True )
    except:
        logger.error("телеграмм отвалился ваще")
        time.sleep(70)
        Connect()

Connect()