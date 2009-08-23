# For handling filenames... 
import os
import pygame
import random
import sys

from pygame.locals import *
from game import *
from Config import *
from State import State

opts = 0
if DoubleBuffer:
	opts = opts | pygame.DOUBLEBUF
if Fullscreen:
	opts = opts | pygame.FULLSCREEN
screen = pygame.display.set_mode(ScreenSize,opts)
pygame.display.set_caption("Title")
pygame.init()

def main(): 
	state = State()
	state.init_state
	state.screen_size = ScreenSize
	state.double_buffer = DoubleBuffer
	state.fullscreen = Fullscreen
	state.framerate = Framerate
	alive = True
	clock = pygame.time.Clock()
	app = game(screen,clock)
	while alive:
		# Events
		if pygame.event.peek(QUIT):
			alive = False
		events = pygame.event.get()
		
		# Pump events to game
		for event in events:
			app.handle_event(event)
			
		# Update state
		update = app.update()
		# Draw
		app.draw()
		
		# Are we done?
		alive = app.alive
		
		# Did we update anything?
		if update: 
			# if so, redraw screen
			pygame.display.flip()
		
		# Regular framerate
		clock.tick(state.framerate)

if __name__ == '__main__':
	main()

