import pygame
import os
from natsort import *

class Loader:
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state
		
	def init_map(self):
		self.map = {}
	
	def contents(self):
		return self.map
	
	def load(self,path):
		if path in self.map:
			return self.map[path]
		else:
			list = self.load_actual(path)
			self.map[path] = list
			return list
			
	def font(self,path,size):
		if path in self.map and size in self.map[path]:
			return self.map[path][size]
		else:
			if not path in self.map:
				self.map[path] = {}
			self.map[path][size] = pygame.font.Font(path,size)
			return self.map[path][size]
			
	def load_font(self,font,size):
		return self.font(os.path.join("res","fonts",font+".ttf"),size)
	
	def load_art(self,filename):
		return self.load(os.path.join("res","art",filename))
	
	def load_actual(self,path):
		list = []
		files = []
		if os.path.isfile(path):
			files.append(path)
		else:
			for file in os.listdir(path):
				if file[0] != '.' and file != "Thumbs.db":
					files.append(os.path.join(path,file))
		files = natsorted(files)
		for file in files:
			list.append(pygame.image.load(file))
		return list
