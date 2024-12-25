
from accest.game_function import *
play_game_mode_lol = True

pg.init()

while Play_Game:

	while arena.mode:
		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

		Update_Arena()

	while plr.die:
		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					from menu import *
					Game = True
					menu.work = True
					Play_Game = False
					plr.die = False
		Update_Die()	


	while pause.mode:
		clock.tick(FPS)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()

		Update_Pause()