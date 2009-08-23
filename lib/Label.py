import pygame
from State import State

class Label:
	# Create a new label with the provided string, SDLFont object, rgb tuple, and coordinate pair.
	def __init__(self,string,font,color,coords):
		state = State()
		self.font = font
		mwidth = font.size("n")[0]
		if mwidth * len(string) > state.screen_size[0] or string.find("\n") > -1:
			chars = int(state.screen_size[0]/mwidth)
			if string.find("\n") > -1:
				pair = string.split("\n")
				str1 = pair[0]
				str2 = pair[1]
			else:
				str1 = string[:chars]
				str2 = string[chars:]
			surface1 = font.render(str1,False,color)
			surface2 = font.render(str2,False,color)
			w = surface1.get_size()[0]
			w2 = surface2.get_size()[0]
			if w2 > w:
				w = w2
			h = surface1.get_size()[1] + surface2.get_size()[1]
			self.surface = pygame.surface.Surface((w,h))
			#self.surface.fill((255,255,255))
			#self.surface.set_colorkey((255,255,255))
			self.surface.blit(surface1,(0,0))
			self.surface.blit(surface2,(0,surface1.get_size()[1]))
		else:
			self.surface = font.render(string,False,color)
		size = self.surface.get_size()
		self.width = size[0]
		self.height = size[1]
		self.coords = coords
		self.alpha = 0
		self.surface.set_alpha(self.alpha)
		self.goal_alpha = 255
		self.shadow = False
	
	# Toggle whether a 50% alpha dropshadow is drawn under this label
	def set_shadow(self,bool):
		self.shadow = bool
	
	def set_y(self,y):
		self.coords = (self.coords[0],y)
	
	def set_x(self,x):
		self.coords = (x,self.coords[1])
		
	def draw(self,surf):
		if self.is_visible():
			if self.shadow:
				self.surface.set_alpha(self.alpha/2)
				surf.blit(self.surface,(self.coords[0]+2,self.coords[1]+2))
				self.surface.set_alpha(self.alpha)
			surf.blit(self.surface,self.coords)
		
	def update(self):
		a = self.alpha
		if self.goal_alpha < self.alpha:
			self.alpha -= 15
			if self.alpha < self.goal_alpha:
				self.alpha = self.goal_alpha
		elif self.goal_alpha > self.alpha:
			self.alpha += 15
			if self.alpha > self.goal_alpha:
				self.alpha = self.goal_alpha
		if a != self.alpha:
			self.surface.set_alpha(self.alpha)
			
	def fade(self,alpha = 0):
		self.goal_alpha = alpha
		
	def is_visible(self):
		return (self.alpha > 0)