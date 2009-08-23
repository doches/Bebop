import os
import pygame
import sys
import math
import random

from pygame.locals import *

sys.path.insert(1,"objects")

sys.path.insert(1, "lib")
from Loader import Loader
from SoundManager import SoundManager

sys.path.insert(1, "screens")
from AuthorScreen import AuthorScreen

class game:
	def __init__(self,surface,clock):
		self.loader = Loader()
		self.loader.init_map()
		self.sound = SoundManager()
		self.sound.init_sound_manager()
		self.clock = clock
		self.alive = True
		self.screen = surface
		self.width = surface.get_size()[0]
		self.height = surface.get_size()[1]
		self.screens = 	[AuthorScreen(3)]
		self.current_screen = 0
		self.screens[self.current_screen].on_focus()
		
	def reset(self):
		self.current_screen = 0
		self.screens[self.current_screen].on_focus()
		#self.layers.append(FPSScreen(self.clock))
	
	def draw(self):
		# INCREDIBLY wasteful...
		self.screen.fill( (0,0,0) )
		self.screens[self.current_screen].draw(self.screen)
		return True
		
	def handle_event(self,event):
		if event.type == QUIT:
			self.alive = False
		elif event.type == KEYDOWN:
			self.changed = True
			if event.key == K_ESCAPE:
				self.alive = False
		try:
			self.screens[self.current_screen].handle_event(event)
		except AttributeError:
			True
	
	def update(self):
		# If the current screen returns FALSE we should move to the next screen in the list.
		retval = self.screens[self.current_screen].update()
		if retval == False:
			if self.current_screen < len(self.screens)-1:
				self.current_screen += 1
				self.screens[self.current_screen].on_focus()
				return True
			else:
				return False
		else:
			return True

