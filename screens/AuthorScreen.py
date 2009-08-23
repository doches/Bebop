from AbstractScreen import AbstractScreen
import os
import pygame
from Loader import Loader
from State import State
from Label import Label
from SoundManager import SoundManager

class AuthorScreen(AbstractScreen):
	def __init__(self,ttl):
		AbstractScreen.__init__(self)
		self.loader = Loader()
		self.state = State()
		large_font = self.loader.load_font("slkscr",72)
		med_font = self.loader.load_font("slkscr",32)
		small_font = self.loader.load_font("slkscr",16)
		x = self.state.screen_size[0]/2
		y = self.state.screen_size[1]/2
		self.labels = [ Label("a game by",med_font,(255,96,96),[x-280,y-30]),
						Label("Doches",large_font,(255,255,255),[x-180,y-10]),
						Label("(aka Trevor Fountain)",small_font,(255,255,255),[x-70,y+50])
		 			  ]
		for label in self.labels:
			label.goal_alpha = 255
		# Set up fade timer
		self.ttl = ttl
		self.sound = SoundManager()
	
	def on_focus(self):
		self.start = pygame.time.get_ticks()
		self.fade_out = self.start + self.ttl*1000
		self.alive = True
		self.sound.start_music(1)
		
	def update(self):
		AbstractScreen.update(self)
		time = pygame.time.get_ticks()
		if time >= self.fade_out and self.alive:
			self.alive = False
			for label in self.labels:
				label.goal_alpha = 0
		elif time >= self.fade_out and self.labels[0].alpha == 0:
			return False
		for label in self.labels:
			label.update()
		return True
	
	def handle_event(self,event):
		if event.type == pygame.locals.KEYDOWN or event.type == pygame.locals.MOUSEBUTTONDOWN:
			self.fade_out = self.start
	
	def draw(self,screen):
		for label in self.labels:
			label.draw(screen)
		return True
