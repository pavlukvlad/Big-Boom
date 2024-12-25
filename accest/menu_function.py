
from accest.menu_files import *
import time
import pygame as pg

pg.init()

class Frame(object):
	def __init__(self, bg, button, work):
		super(Frame, self).__init__()
		self.bg = bg
		self.button = button
		self.work = work

menu = Frame(bg_menu_img, 1, False)
credit = Frame(bg_credit_img, None, False)
helps = Frame(bg_help_img, None, False)
rating = Frame(bg_rating_img, None, False)
option = Frame(bg_option_img, 1, False)
start = Frame(present_bg_img, None, True)


def Update_Credit_scr():
	scr.blit(credit.bg, (0, 0))
	pg.display.update()

def Update_Help_scr():
	scr.blit(helps.bg, (0, 0))
	pg.display.update()

def Update_Rating_scr():
	scr.blit(rating.bg, (0, 0))
	pg.display.update()

def Update_Menu_scr():
	scr.blit(menu.bg, (0, 0))
	b_Play()
	b_Rating()
	b_Options()
	b_Help()
	b_Credit()
	pg.display.update()

def Update_start_scr():
	start_sound.play(0)
	scr.blit(present_bg_img, (0, 0))
	pg.display.update()
	time.sleep(0.5)




class Button(object):
	def __init__(self, x, y, mode):
		super(Button, self).__init__()
		self.x = x
		self.y = y
		self.mode = mode

bcredit = Button(0, 0, None)
bhelp = Button(0, 0, None)
boption = Button(0, 0, None)
brating = Button(0, 0, None)
bplay = Button(0, 0, None)
sound = Button(0, 0, True)
music = Button(0, 0, True)
gamemode = Button(0, 0, 2)
exit = Button(0, 0, None)



def b_Play():
	if menu.button == 1 and bplay.x > -30:
		bplay.x += -8

	elif menu.button != 1 and bplay.x < 0:
		bplay.x += 8

	scr.blit(play_ui_img, (bplay.x, bplay.y))


def b_Rating():
	if menu.button == 2 and brating.x > -30:
		brating.x += -8

	elif menu.button != 2 and brating.x < 0:
		brating.x += 8

	scr.blit(rating_ui_img, (brating.x, brating.y))



def b_Options():
	if menu.button == 3 and boption.x > -30:
		boption.x += -8

	elif menu.button != 3 and boption.x < 0:
		boption.x += 8

	scr.blit(option_ui_img, (boption.x, boption.y))


def b_Help():
	if menu.button == 5:
		bhelp.mode = help_ui_img[1]

	elif menu.button != 5:
		bhelp.mode = help_ui_img[0]

	scr.blit(bhelp.mode, (bhelp.x, bhelp.y))

def b_Credit():
	if menu.button == 4:
		bcredit.mode = credit_ui_img[1]

	elif menu.button != 4:
		bcredit.mode = credit_ui_img[0]


	scr.blit(bcredit.mode, (bcredit.x, bcredit.y))


def Sound_On():
	if option.button == 1 and sound.x > -20:
		sound.x += -5

	elif option.button != 1 and sound.x < 0:
		sound.x += 5

	if sound.mode:
		scr.blit(sound_ui_img_1, (sound.x, sound.y))
		
	elif not sound.mode:
		scr.blit(sound_ui_img_2, (sound.x, sound.y))


def Music_On():	
	if option.button == 2 and music.x > -20:
		music.x += -5

	elif option.button != 2 and music.x < 0:
		music.x += 5


	if music.mode:
		scr.blit(music_ui_img_1, (music.x, music.y))

	elif not music.mode:
		scr.blit(music_ui_img_2, (music.x, music.y))

	

def Game_Mode_of_Game():
	if option.button == 3 and gamemode.x > -20:
		gamemode.x += -5

	elif option.button != 3 and gamemode.x < 0:
		gamemode.x += 5

	if gamemode.mode == 1:
		scr.blit(gamemode_ui_img_1, (gamemode.x, gamemode.y))

	elif gamemode.mode == 2:
		scr.blit(gamemode_ui_img_2, (gamemode.x, gamemode.y))

	elif gamemode.mode == 3:
		scr.blit(gamemode_ui_img_3, (gamemode.x, gamemode.y))


def exit_move():
	if option.button == 4 and exit.x > -30:
		exit.x += -5

	elif option.button != 4 and exit.x < 0:
		exit.x += 5

	scr.blit(exit_ui_img, (exit.x, exit.y))




def Update_Option_scr():
	scr.blit(option.bg, (0, 0))
	Sound_On()
	Music_On()
	Game_Mode_of_Game()
	exit_move()
	pg.display.update()

def QUIT():
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		elif event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					button_sound.play(0)

					menu.work = True

					if credit.work:
						credit.work = False
						menu.work = True

					elif start.work:
						start.work = False
						menu.work = True

					elif rating.work:
						rating.work = False
						menu.work = True

					elif helps.work:
						helps.work = False
						menu.work = True