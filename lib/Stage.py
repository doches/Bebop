import pygame
import os
from Loader import Loader

class Stage:
	__shared_state = {}
	
	def __init__(self):
		self.__dict__ = self.__shared_state
		
	def init_stage(self):
		self.objects = []
	
	def attach(self,object):
		self.objects.append(object)
	
	def draw(self,surface):
		for obj in self.objects:
			obj.draw(surface)
	
	def update(self):
		to_remove = []
		for obj in self.objects:
			if not obj.update():
				to_remove.append(obj)
		for obj in to_remove:
			self.objects.remove(obj)
		return (len(self.objects) > 0)

class Ephemeral:
	def __init__(self,coords):
		self.coords = coords

class Click(Ephemeral):
	def __init__(self,coords):
		Ephemeral.__init__(self,coords)
		self.index = -1
		self.surf = Loader().load(os.path.join("res","art","click"))
		self.coords = [self.coords[0] - self.surf[0].get_size()[0]/2,self.coords[1] - self.surf[0].get_size()[1]/2]
	
	def update(self):
		self.index += 0.5
		return (self.index < len(self.surf))
	
	def draw(self,surf):
		surf.blit(self.surf[int(self.index)],self.coords)