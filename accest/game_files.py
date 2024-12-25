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
bg_music_play_arena = False

keys = pg.key.get_pressed()
Play_Game = True
clock = pg.time.Clock()
FPS = 20

screen_widht = 800
screen_height = 600

scr = pg.display.set_mode((screen_widht, screen_height))

run_left_img = [pg.image.load(".data/images/player/left/1.png"),
pg.image.load(".data/images/player/left/2.png"), 
pg.image.load(".data/images/player/left/3.png"),
pg.image.load(".data/images/player/left/4.png")
]

run_right_img = [pg.image.load(".data/images/player/right/1.png"),
pg.image.load(".data/images/player/right/2.png"),
pg.image.load(".data/images/player/right/3.png"),
pg.image.load(".data/images/player/right/4.png")
]

run_up_img = [pg.image.load(".data/images/player/up/1.png"),
pg.image.load(".data/images/player/up/2.png"),
pg.image.load(".data/images/player/up/3.png"),
pg.image.load(".data/images/player/up/4.png")
]

run_down_img = [pg.image.load(".data/images/player/down/1.png"),
pg.image.load(".data/images/player/down/2.png"),
pg.image.load(".data/images/player/down/3.png"),
pg.image.load(".data/images/player/down/4.png")
]

die_img = pg.image.load(".data/images/player/die.png")


basic_bomb_img = [pg.image.load(".data/images/booms/basic/1.png"),
pg.image.load(".data/images/booms/basic/2.png"),
pg.image.load(".data/images/booms/basic/3.png"),
pg.image.load(".data/images/booms/basic/4.png")
]

bullet_img = pg.image.load(".data/images/booms/small.png")

basic_boom_img = [
pg.image.load(".data/images/booms/boom/1.png"),
pg.image.load(".data/images/booms/boom/2.png"),
pg.image.load(".data/images/booms/boom/3.png"), 
pg.image.load(".data/images/booms/boom/4.png"),
pg.image.load(".data/images/booms/boom/5.png"), 
pg.image.load(".data/images/booms/boom/6.png"), 
pg.image.load(".data/images/booms/boom/7.png"), 
pg.image.load(".data/images/booms/boom/8.png"), 
pg.image.load(".data/images/booms/boom/9.png"),
pg.image.load(".data/images/booms/boom/10.png")
]

bonus_health_img = pg.image.load(".data/images/bonus/hp.png")

load_bg_img = [
pg.image.load(".data/images/bg/load_1.jpg"),
pg.image.load(".data/images/bg/load_2.jpg"),
pg.image.load(".data/images/bg/load_3.jpg")
]

counter_bg_img = pg.image.load(".data/images/bg/arena.png")
game_bg_img = pg.image.load(".data/images/bg/bg_arena.png")
pause_bg_img = pg.image.load(".data/images/bg/pause_bg.png")
game_over_img = pg.image.load(".data/images/bg/die.png")

health_ui_img = [
pg.image.load(".data/images/ui/health/1.png"),
pg.image.load(".data/images/ui/health/2.png"),
pg.image.load(".data/images/ui/health/3.png"),
pg.image.load(".data/images/ui/health/4.png")
]

stamina_ui_img = [
pg.image.load(".data/images/ui/stamina/1.png"),
pg.image.load(".data/images/ui/stamina/2.png"),
pg.image.load(".data/images/ui/stamina/3.png"),
pg.image.load(".data/images/ui/stamina/4.png"),
pg.image.load(".data/images/ui/stamina/5.png"),
pg.image.load(".data/images/ui/stamina/6.png"),
pg.image.load(".data/images/ui/stamina/7.png"),
pg.image.load(".data/images/ui/stamina/8.png"),
]

run_left_Q_img = [pg.image.load(".data/images/player/Q/left/1.png"),
pg.image.load(".data/images/player/Q/left/2.png"), 
pg.image.load(".data/images/player/Q/left/3.png"),
pg.image.load(".data/images/player/Q/left/4.png")
]

run_right_Q_img = [pg.image.load(".data/images/player/Q/right/1.png"),
pg.image.load(".data/images/player/Q/right/2.png"),
pg.image.load(".data/images/player/Q/right/3.png"),
pg.image.load(".data/images/player/Q/right/4.png")
]

run_up_Q_img = [pg.image.load(".data/images/player/Q/up/1.png"),
pg.image.load(".data/images/player/Q/up/2.png"),
pg.image.load(".data/images/player/Q/up/3.png"),
pg.image.load(".data/images/player/Q/up/4.png")
]

run_down_Q_img = [pg.image.load(".data/images/player/Q/down/1.png"),
pg.image.load(".data/images/player/Q/down/2.png"),
pg.image.load(".data/images/player/Q/down/3.png"),
pg.image.load(".data/images/player/Q/down/4.png")
]

run_aura_img = [pg.image.load(".data/images/player/run/1.png"),
pg.image.load(".data/images/player/run/2.png"),
pg.image.load(".data/images/player/run/3.png"),
pg.image.load(".data/images/player/run/4.png")
]

mega_bullet_sound = (None) # Will Soon
bullet_sound = pg.mixer.Sound(".data/sound/bullet.wav")
arena_sound = pg.mixer.Sound(".data/sound/arena.mp3")
new_wawe_sound = (None) # Will soon
dash_sound = pg.mixer.Sound(".data/sound/Q.wav")
boom_sound = pg.mixer.Sound(".data/sound/boom.wav")
dead_sound = pg.mixer.Sound(".data/sound/die_fun.wav")
game_over_sound = pg.mixer.Sound(".data/sound/game_over_fun.wav")