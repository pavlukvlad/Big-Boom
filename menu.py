import sys
from accest.menu_function import *
from accest.game_function import *
bg_arena_play = True

while Game:
	if start.work:
		QUIT()
 
		Update_start_scr()

		start.work = False
		menu.work = True
		bg_arena_play = False

		if not bg_music_play:
			game_over_sound.play(-1)
			menu_sound.play(-1)
			bg_music_play = True


	elif menu.work:
		arena_sound.set_volume(0)
		game_over_sound.set_volume(0)
		menu_sound.set_volume(50)

		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_DOWN:
					button_sound.play(0)

					if menu.button > 0 and menu.button < 5:
						menu.button += 1

					elif menu.button == 5:
						menu.button -= 4

				elif event.key == pg.K_UP:
					button_sound.play(0)

					if menu.button >= 0 and menu.button < 6:
						menu.button -= 1

					if menu.button == 0:
						menu.button += 5


				elif event.key == pg.K_RETURN:
					button_sound.play(0)

					if menu.button == 1:
						plr.die =  False
						plr.health = 3
						plr.x = 400
						plr.y = 300

						arena_mode = True
						menu.work = False

					elif menu.button == 2:
						rating.work = True
						menu.work = False

					elif menu.button == 3:
						option.work = True
						menu.work = False

					elif menu.button == 4:
						credit.work = True
						menu.work = False

					elif menu.button == 5:
						helps.work = True
						menu.work = False

		Update_Menu_scr()



# help 
	elif helps.work:


		QUIT()
		Update_Help_scr()


# credit
	elif credit.work:


		QUIT()

		Update_Credit_scr()


# option
	elif option.work:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_DOWN:
					button_sound.play(0)

					if option.button > 0 and option.button < 4:
						option.button += 1

					elif option.button == 4:
						option.button -= 3

				elif event.key == pg.K_UP:
					button_sound.play(0)

					if option.button >= 0 and option.button < 5:
						option.button -= 1

					if option.button == 0:
						option.button += 4


				elif event.key == pg.K_RETURN:
					button_sound.play(0)

					if option.button == 1 and sound.mode:
						sound.mode = False
						sound_on = False


					elif option.button == 2 and music.mode:
						music.mode = False
						music_on = False


					elif option.button == 2 and not music.mode:
						music.mode = True
						music_on = True





					elif option.button == 1 and not sound.mode:
						sound.mode = True
						sound_on = True

					elif option.button == 3 and gamemode.mode == 3:
						gamemode.mode = 1

					elif option.button == 3:
						gamemode.mode += 1

					elif option.button == 4:
						menu.work = True
						option.work = False

		Update_Option_scr()


# rating
	elif rating.work:

		QUIT()

		Update_Rating_scr()

	elif arena_mode:
		if not bg_arena_play:
			arena_sound.play(-1)
			bg_arena_play = True

		arena.mode = True
		arena_mode = False


	elif arena.mode:
		boom_sound.set_volume(25)
		menu_sound.set_volume(0)
		arena_sound.set_volume(50)

		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					press_Q()

		Update_Arena()

	elif plr.die:
		boom_sound.set_volume(0)

		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					menu.work = True
					plr.die = False
					start_arena()
		Update_Die()	


	elif pause.mode:

		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

		Update_Pause()





 