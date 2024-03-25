import pygame 
from functions import *
from GPTAPI import *


# for screen size and adjustment of objects on screen 
WIDTH, HEIGHT = 1400, 800

stars = generate_stars(100, WIDTH, HEIGHT)


# Initialize text input variables
question = ""
response, context = open_ai_chat(question, context)
