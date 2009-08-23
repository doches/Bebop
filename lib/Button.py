import pygame
from pygame.locals import *
from Loader import Loader

class Button:
	def __init__(self,string,pos,size=16):
		self.pos = pos
		self.string = None
		self.tsize = size
		self.bg_color = (64,64,64)
		self.hg_color = (128,128,128)
		self.write(string)
		self.message = string
	
	def write(self,string):
		if string == self.string:
			return False

		load = Loader()
		text_color = (255,255,255)
		border_color = (196,196,196)
		font = load.load_font("slkscr",self.tsize)
		text = font.render(string,False,text_color)
		self.text = text
		self.surface = pygame.Surface((text.get_size()[0]+20,text.get_size()[1]+14))
		self.surface.fill(self.bg_color)
		self.surface.blit(text,(10,7))
		pygame.draw.rect(self.surface,border_color,pygame.Rect(0,0,self.surface.get_size()[0]-1,self.surface.get_size()[1]-1),2)
		self.size = self.surface.get_size()
		self.string = string
		self.highlight = False
		return True
	
	def click(self,pos):
		return self.mouse_in(pos)
	
	def draw(self,surface):
		surface.blit(self.surface,self.pos)
	
	def mouse_in(self,coords):
		if coords[0] > self.pos[0] and coords[0] < self.pos[0] + self.size[0] and coords[1] > self.pos[1] and coords[1] < self.pos[1] + self.size[1]:
			if not self.highlight:
				pygame.draw.rect(self.surface,self.hg_color,pygame.Rect(2,2,self.size[0]-4,self.size[1]-4),0)
				self.surface.blit(self.text,(10,7))
				self.highlight = True
			return True
		if self.highlight:
			pygame.draw.rect(self.surface,self.bg_color,pygame.Rect(2,2,self.size[0]-4,self.size[1]-4),0)
			self.surface.blit(self.text,(10,7))
			self.highlight = False
		return False
