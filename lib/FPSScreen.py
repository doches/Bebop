import pygame
from pygame.locals import *
from Config import *
from State import State
from Loader import Loader

FPSCounter = 10

class FPSScreen:
	def __init__(self,clock):
		self.font = Loader().load_font("slkscr",16)
		self.clock = clock
		self.render()
		self.tick = 0
		self.state = State()
	
	def render(self):
		self.fps = self.font.render(str(int(self.clock.get_fps()*100)/100.0),False,(255,255,255))
		self.size = self.fps.get_size()
		
	def update(self):
		self.tick += 1
		if self.tick > FPSCounter:
			self.tick = 0
			self.render()
	
	def draw(self,surface):
		surface.blit(self.fps,(self.state.screen_size[0]-self.size[0],self.state.screen_size[1] - self.size[1]))