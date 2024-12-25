import pygame as pg
from time import sleep
from random import choice, randint
import sys

pg.init()

Game = True
screen_menu = False
files_type = True
bg_music_play = False

music_on = True
sound_on = True
screen_game = False
FPS = 15
arena_mode = False


clock = pg.time.Clock()

screen_widht = 800
screen_height = 600

scr = pg.display.set_mode((screen_widht, screen_height))


present_bg_img = pg.image.load(".data/images/bg/present.jpg")


bg_menu_img = pg.image.load(".data/images/bg/menu_bg.jpg")
bg_credit_img = pg.image.load(".data/images/bg/credit_bg.jpg")
bg_option_img = pg.image.load(".data/images/bg/option_bg.jpg")
bg_help_img = pg.image.load(".data/images/bg/help_bg.jpg")
bg_pause_img = pg.image.load(".data/images/bg/pause_bg.png")
bg_rating_img = pg.image.load(".data/images/bg/rating_bg.jpg")





play_ui_img = pg.image.load(".data/images/ui/button/play.png")
rating_ui_img = pg.image.load(".data/images/ui/button/rating.png")
option_ui_img = pg.image.load(".data/images/ui/button/option.png")

help_ui_img = [
pg.image.load(".data/images/ui/button/help.png"),
pg.image.load(".data/images/ui/button/help_on.png")
]


credit_ui_img = [
pg.image.load(".data/images/ui/button/credit.png"),
pg.image.load(".data/images/ui/button/credit_on.png")
]




gamemode_ui_img_1 = pg.image.load(".data/images/ui/button/gamemode_easy.png")
gamemode_ui_img_2 = pg.image.load(".data/images/ui/button/gamemode_normal.png")
gamemode_ui_img_3 = pg.image.load(".data/images/ui/button/gamemode_expert.png")

sound_ui_img_1 = pg.image.load(".data/images/ui/button/sound_on.png")
sound_ui_img_2 = pg.image.load(".data/images/ui/button/sound_off.png")

music_ui_img_1 = pg.image.load(".data/images/ui/button/music_on.png")
music_ui_img_2 = pg.image.load(".data/images/ui/button/music_off.png")


exit_ui_img = pg.image.load(".data/images/ui/button/exit_lol.png")


menu_sound = pg.mixer.Sound(".data/sound/menu.mp3")
button_sound = pg.mixer.Sound(".data/sound/button.wav")
start_sound = pg.mixer.Sound(".data/sound/start.wav")