
from accest.demo_bomb import *

import time
import pygame as pg
from sys import *

pg.init()

helth_stamina = 0
st_error = False
times = 0
need_time = int(times * 1.5)
cadr = 0
second = 0
minutes = 0
hour = 0
wawe = 1
crystal = 0
timer = f"{second}:{minutes}:{hour}"

h1 = pg.font.Font('.data/impact.otf', 16)
h3 = pg.font.Font(".data/impact.otf", 12)

wawe_text = h1.render(f'Wawe {wawe}', True, (200 ,200 ,200 ))
time_text = h3.render(f"{timer}", True, (200 ,200 ,200 ))
crystal_text = h3.render(f"{crystal}", True, (200 ,200 ,200 ))
error_St_text = h3.render("You lack stamina", True, (150, 0, 0))

class Game(object):
	def __init__(self, mode ,bg, wawe, button):
		super(Game, self).__init__()
		self.mode = mode
		self.bg = bg
		self.wawe = wawe
		self.button = button

arena = Game(True, game_bg_img, 1, None)
pause = Game(False, pause_bg_img, None, 1)

     
class Button(object):
	def __init__(self, x, y):
		super(But, self).__init__()
		self.x = x
		self.y = y

class Player(object):
	def __init__(self, x, y, height, width, health, stamina, vel, AnimCount, mode, idle, die, Q, Aura):
		super(Player, self).__init__()
		self.x = x
		self.y = y
		self.height = height
		self.width = width

		self.health = health
		self.stamina = stamina

		self.vel = vel

		self.AnimCount = AnimCount
		self.mode = mode
		self.idle = idle
		self.die = die
		self.Q = Q
		self.Aura = Aura

plr = Player(400, 300, 32, 32, 3, 7, 3, 0 ,'down', True, False, False, False)




# 1
AnimCount1 = [0, 0, 0, 0]
bomb_y1 = [randint(-80, -20), randint(-80, -20), randint(-80, -20), randint(-80, -20)]
bomb_x1 = [randint(75, 150), randint(162, 312), randint(324, 474), randint(486, 725)]
bomb_boom1 = [False, False, False, False]
#bomb_width1 = 25
#bomb_height1 = 25


# 2
AnimCount2 = [0, 0, 0, 0]
bomb_y2 = [randint(-80, -20), randint(-80, -20), randint(-80, -20), randint(-80, -20)]
bomb_x2 = [randint(75, 150), randint(162, 312), randint(324, 474), randint(486, 725)]
bomb_boom2 = [False, False, False, False]
#bomb_width2 = 25
#bomb_height2 = 25

# 3
AnimCount3 = [0, 0, 0, 0]
bomb_y3 = [randint(-80, -20), randint(-80, -20), randint(-80, -20), randint(-80, -20)]
bomb_x3 = [randint(75, 150), randint(162, 312), randint(324, 474), randint(486, 725)]
bomb_boom3 = [False, False, False, False]
#bomb_width3 = 25
#bomb_height3 = 25


vel = 8

def bomb1():
	global AnimCount1
	global bomb_x1
	global bomb_y1
	global bomb_boom1

	for num in range(len(bomb_boom1)):

		if bomb_y1[num] <= 530 and not bomb_boom1[num] and not plr.die:
			bomb_y1[num] += vel

		elif bomb_y1[num] >= 530:
			bomb_boom1[num] = True
			boom_sound.play(0)			

		if AnimCount1[num] + 1 >= 20 and not bomb_boom1[num]:
			AnimCount1[num] = 0

		if not bomb_boom1[num]:
			scr.blit(basic_bomb_img[AnimCount1[num] // 5], (bomb_x1[num], bomb_y1[num]))
			AnimCount1[num] += 1

		elif bomb_boom1[num] and AnimCount1[num] < 20:
			scr.blit(basic_boom_img[AnimCount1[num] // 2], (bomb_x1[num], bomb_y1[num]))
			AnimCount1[num] += 1

		if bomb_boom1[0] and bomb_boom1[1] and bomb_boom1[2] and bomb_boom1[3]:
			AnimCount1[0] = 0
			AnimCount1[1] = 0
			AnimCount1[2] = 0
			AnimCount1[3] = 0

			bomb_y1[0] = randint(-80, -20)
			bomb_x1[0] = randint(75, 150)
			bomb_boom1[0] = False

			bomb_y1[1] = randint(-80, -20)
			bomb_x1[1] = randint(162, 312)
			bomb_boom1[1] = False

			bomb_y1[2] = randint(-80, -20)
			bomb_x1[2] = randint(324, 474)
			bomb_boom1[2] = False


			bomb_y1[3] = randint(-80, -20)
			bomb_x1[3] = randint(486, 725)
			bomb_boom1[3] = False



def bomb2():
	global AnimCount2
	global bomb_x2
	global bomb_y2
	global bomb_boom2

	for num in range(len(bomb_boom2)):

		if bomb_y2[num] <= 530 and not bomb_boom2[num] and not plr.die:
			bomb_y2[num] += vel

		elif bomb_y2[num] >= 530:
			bomb_boom2[num] = True
			boom_sound.play(0)			

		if AnimCount2[num] + 1 >= 20 and not bomb_boom2[num]:
			AnimCount2[num] = 0

		if not bomb_boom2[num]:
			scr.blit(basic_bomb_img[AnimCount2[num] // 5], (bomb_x2[num], bomb_y2[num]))
			AnimCount2[num] += 1

		elif bomb_boom2[num] and AnimCount2[num] < 20:
			scr.blit(basic_boom_img[AnimCount2[num] // 2], (bomb_x2[num], bomb_y2[num]))
			AnimCount2[num] += 1
			#bomb_x2[num] = 1000

		if bomb_boom2[0] and bomb_boom2[1] and bomb_boom2[2] and bomb_boom2[3]:
			AnimCount2[0] = 0
			AnimCount2[1] = 0
			AnimCount2[2] = 0
			AnimCount2[3] = 0
			
			bomb_y2[0] = randint(-80, -20)
			bomb_x2[0] = randint(75, 150)
			bomb_boom2[0] = False

			bomb_y2[1] = randint(-80, -20)
			bomb_x2[1] = randint(162, 312)
			bomb_boom2[1] = False


			bomb_y2[2] = randint(-80, -20)
			bomb_x2[2] = randint(324, 474)
			bomb_boom2[2] = False


			bomb_y2[3] = randint(-80, -20)
			bomb_x2[3] = randint(486, 725)
			bomb_boom2[3] = False


def bomb3():
	global AnimCount3
	global bomb_x3
	global bomb_y3
	global bomb_boom3

	for num in range(len(bomb_boom3)):

		if bomb_y3[num] <= 530 and not bomb_boom3[num] and not plr.die:
			bomb_y3[num] += vel

		if bomb_y3[num] >= 530:
			bomb_boom3[num] = True
			boom_sound.play(0)

		if AnimCount3[num] + 1 >= 20 and not bomb_boom3[num]:
			AnimCount3[num] = 0

		if not bomb_boom3[num]:
			scr.blit(basic_bomb_img[AnimCount3[num] // 5], (bomb_x3[num], bomb_y3[num]))
			AnimCount3[num] += 1

		elif bomb_boom3[num] and AnimCount3[num] < 20:
			scr.blit(basic_boom_img[AnimCount3[num] // 2], (bomb_x3[num], bomb_y3[num]))
			AnimCount3[num] += 1

		if bomb_boom3[0] and bomb_boom3[1] and bomb_boom3[2] and bomb_boom3[3]:
			AnimCount3[0] = 0
			AnimCount3[1] = 0
			AnimCount3[2] = 0
			AnimCount3[3] = 0
			
			bomb_y3[0] = randint(-80, -20)
			bomb_x3[0] = randint(75, 150)
			bomb_boom3[0] = False

			bomb_y3[1] = randint(-80, -20)
			bomb_x3[1] = randint(162, 312)
			bomb_boom3[1] = False


			bomb_y3[2] = randint(-80, -20)
			bomb_x3[2] = randint(324, 474)
			bomb_boom3[2] = False


			bomb_y3[3] = randint(-80, -20)
			bomb_x3[3] = randint(486, 725)
			bomb_boom3[3] = False



def Player_Move():
	global helth_stamina
	global st_error
	keys = pg.key.get_pressed()

	if keys[pg.K_e]:
		plr.vel = 2
		helth_stamina += 1

	elif keys[pg.K_a]:
		plr.mode = "left"
		plr.x -= plr.vel

	elif keys[pg.K_d]:
		plr.mode = "right"
		plr.x += plr.vel

	if keys[pg.K_w]:
		plr.mode = "up"
		plr.y -= plr.vel

	elif keys[pg.K_s]:
		plr.mode = "down"
		plr.y += plr.vel

	if keys[pg.K_LSHIFT]:
		if plr.stamina > 0:
			plr.Aura = True
			plr.vel = 6
			helth_stamina = 0

		else:
			plr.Aura = False
			if not st_error:
				st_error = True
			plr.vel = 2
			helth_stamina = 0


	if not keys[pg.K_LSHIFT]:
		plr.Aura = False
		plr.vel = 4

	elif not keys[pg.K_a] and not keys[pg.K_d] and not keys[pg.K_w] and not keys[pg.K_s]:
		plr.idle = True

	if keys[pg.K_a] or keys[pg.K_d] or keys[pg.K_w] or keys[pg.K_s]:
		plr.idle = False

def Player_Die():
	if bomb_x1[0] > plr.x - plr.width and bomb_x1[0] < plr.x + plr.width and bomb_y1[0] > plr.y - plr.height and bomb_y1[0] < plr.y + plr.height and not bomb_boom1[0]:
		bomb_boom1[0] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x1[1] > plr.x - plr.width and bomb_x1[1] < plr.x + plr.width and bomb_y1[1] > plr.y - plr.height and bomb_y1[1] < plr.y + plr.height and not bomb_boom1[1]:
		bomb_boom1[1] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x1[2] > plr.x - plr.width and bomb_x1[2] < plr.x + plr.width and bomb_y1[2] > plr.y - plr.height and bomb_y1[2] < plr.y + plr.height and not bomb_boom1[2]:
		bomb_boom1[2] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x1[3] > plr.x - plr.width and bomb_x1[3] < plr.x + plr.width and bomb_y1[3] > plr.y - plr.height and bomb_y1[3] < plr.y + plr.height and not bomb_boom1[3]:
		bomb_boom1[3] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x2[0] > plr.x - plr.width and bomb_x2[0] < plr.x + plr.width and bomb_y2[0] > plr.y - plr.height and bomb_y2[0] < plr.y + plr.height and not bomb_boom2[0]:
		bomb_boom2[0] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x2[1] > plr.x - plr.width and bomb_x2[1] < plr.x + plr.width and bomb_y2[1] > plr.y - plr.height and bomb_y2[1] < plr.y + plr.height and not bomb_boom2[1]:
		bomb_boom2[1] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x2[2] > plr.x - plr.width and bomb_x2[2] < plr.x + plr.width and bomb_y2[2] > plr.y - plr.height and bomb_y2[2] < plr.y + plr.height and not bomb_boom2[2]:
		bomb_boom2[2] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x2[3] > plr.x - plr.width and bomb_x2[3] < plr.x + plr.width and bomb_y2[3] > plr.y - plr.height and bomb_y2[3] < plr.y + plr.height and not bomb_boom2[3]:
		bomb_boom2[3] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x3[0] > plr.x - plr.width and bomb_x3[0] < plr.x + plr.width and bomb_y3[0] > plr.y - plr.height and bomb_y3[0] < plr.y + plr.height and not bomb_boom3[0]:
		bomb_boom3[0] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x3[1] > plr.x - plr.width and bomb_x3[1] < plr.x + plr.width and bomb_y3[1] > plr.y - plr.height and bomb_y3[1] < plr.y + plr.height and not bomb_boom3[1]:
		bomb_boom3[1] = True
		plr.health -= 1
		dead_sound.play(0)
		boom_sound.play(0)

	if bomb_x3[2] > plr.x - plr.width and bomb_x3[2] < plr.x + plr.width and bomb_y3[2] > plr.y - plr.height and bomb_y3[2] < plr.y + plr.height and not bomb_boom3[2]:
		bomb_boom3[2] = True
		plr.health -= 1
		dead_sound.play(0)


	if bomb_x3[3] > plr.x - plr.width and bomb_x3[3] < plr.x + plr.width and bomb_y3[3] > plr.y - plr.height and bomb_y3[3] < plr.y + plr.height and not bomb_boom3[3]:
		bomb_boom3[3] = True
		plr.health -= 1
		dead_sound.play(0)
		dead_sound.set_volume(100)


	if plr.health < 0:
		arena_sound.set_volume(0)
		game_over_sound.set_volume(50)
		plr.die = True
		arena.mode = False



def Update_Arena():
	from menu import music_on, sound_on
	scr.blit(arena.bg, (0, 0))
	Player_Move()
	bari()
	time()

	if plr.AnimCount + 1 >= 20:
		plr.AnimCount = 0

	if plr.AnimCount == 4 and plr.Q:
		plr.Q = False
		plr.AnimCount = 0

	if plr.mode == "left" and not plr.Q:
		scr.blit(run_left_img[plr.AnimCount // 5], (plr.x, plr.y))
		plr.AnimCount += 1

	elif plr.mode == "right" and not plr.Q:
		scr.blit(run_right_img[plr.AnimCount // 5], (plr.x, plr.y))
		plr.AnimCount += 1

	elif plr.mode == "up" and not plr.Q:
		scr.blit(run_up_img[plr.AnimCount // 5], (plr.x, plr.y))
		plr.AnimCount += 1

	elif plr.mode == "down" and not plr.Q:
		scr.blit(run_down_img[plr.AnimCount // 5], (plr.x, plr.y))
		plr.AnimCount += 1


	if plr.mode == "down" and plr.Q:
		if plr.AnimCount == 0:
			plr.stamina -= 2

		plr.y += 16
		scr.blit(run_down_Q_img[plr.AnimCount // 1], (plr.x, plr.y - 96))
		plr.AnimCount += 1

	elif plr.mode == "up" and plr.Q:
		if plr.AnimCount == 0:
			plr.stamina -= 2
			
		plr.y -= 16
		scr.blit(run_up_Q_img[plr.AnimCount // 1], (plr.x, plr.y + 96))
		plr.AnimCount += 1

	elif plr.mode == "left" and plr.Q:
		if plr.AnimCount == 0:
			plr.stamina -= 2
			
		plr.x -= 16
		scr.blit(run_left_Q_img[plr.AnimCount // 1], (plr.x + 96, plr.y))
		plr.AnimCount += 1

	elif plr.mode == "right" and plr.Q:
		if plr.AnimCount == 0:
			plr.stamina -= 2
			
		plr.x += 16
		scr.blit(run_right_Q_img[plr.AnimCount // 1], (plr.x - 96, plr.y))
		plr.AnimCount += 1

	if plr.Aura:
		scr.blit(run_aura_img[plr.AnimCount // 5], (plr.x, plr.y))

	bomb1()

	if bomb_y1[0] >= 100 and bomb_y1[1] >= 100 and bomb_y1[2] >= 100 and bomb_y1[3] >= 100 or bomb_y2[0] >= 100 or bomb_y2[1] >= 100 or bomb_y2[2] >= 100 or bomb_y2[3] >= 100:
		bomb2()

	if bomb_y2[0] >= 100 and bomb_y2[1] >= 100 and bomb_y2[2] >= 100 and bomb_y2[3] >= 100 or bomb_y3[0] >= 100 or bomb_y3[1] >= 100 or bomb_y3[2] >= 100 or bomb_y3[3] >= 100:
		bomb3()

	Player_Die()
	scr.blit(counter_bg_img, (0, 0))
	scr.blit(wawe_text, (375, 11))
	scr.blit(time_text, (388, 31))
	scr.blit(crystal_text, (770, 39))

	if st_error:
		scr.blit(error_St_text, (150, 55))

	scr.blit(stamina_ui_img[plr.stamina], (0, 0))
	scr.blit(health_ui_img[plr.health], (0, 0))
	pg.display.flip()



def bari():
	if plr.y <= 55:
		plr.y += plr.vel

	if plr.x <= 55:
		plr.x += plr.vel

	if plr.y >= 525:
		plr.y -= plr.vel

	if plr.x >= 720:
		plr.x -= plr.vel

def Update_Die():
	scr.blit(arena.bg, (0, 0))

	bomb1()
	bomb2()
	bomb3()
	scr.blit(counter_bg_img, (0, 0))
	scr.blit(die_img, (plr.x, plr.y))
	scr.blit(game_over_img, (0, 0))
	
	pg.display.flip()


def Update_Pause():
	scr.blit(pause.bg, (0, 0))

	pg.display.update() 

def start_arena():
	global second
	global hour
	global minutes
	global wawe
	global helth_stamina
	global vel

	vel = 8
	second = 0
	hour = 0
	minutes = 0
	wawe = 1
	helth_stamina = 0
	plr.stamina = 7
	plr.health = 3
	bomb_boom1[0] = True
	bomb_boom1[1] = True
	bomb_boom1[2] = True
	bomb_boom1[3] = True
	bomb_boom2[0] = True
	bomb_boom2[1] = True
	bomb_boom2[2] = True
	bomb_boom2[3] = True
	bomb_boom3[0] = True
	bomb_boom3[1] = True
	bomb_boom3[2] = True
	bomb_boom3[3] = True

def time():
	global second
	global hour
	global minutes
	global timer
	global cadr
	global wawe_text
	global wawe
	global time_text
	global vel
	global st_error
	global helth_stamina

	cadr += 1

	if cadr == FPS:
		second += 1
		cadr = 1
		st_error = False
		helth_stamina += 1
		if plr.Aura:
			plr.stamina -= 1

	if helth_stamina >= 20:
		if plr.stamina < 7:
			plr.stamina += 1

		helth_stamina = 0

	if second == 60:
		minutes += 1
		second = 1
		wawe += 1

		if vel < 19:
			vel += 1

	if minutes == 60:
		hour += 1
		minutes = 1

	timer = f"{second}:{minutes}:{hour}"
	wawe_text = h1.render(f'Wawe {wawe}', True, (200 ,200 ,200 ))
	time_text = h3.render(f"{timer}", True, (200 ,200 ,200 ))

def press_Q():
	global st_error

	if plr.stamina > 1:
		plr.Q = True
		plr.AnimCount = 0
		dash_sound.play(0)

	elif plr.stamina <= 2:
		st_error = True
