import pygame
import os
import random
from time import time

class SoundManager:
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state
	
	# Initialize the sound manager, loading files from disk and whatnot.
	def init_sound_manager(self):
		pygame.mixer.init
		self.sounds = {}
		self.music = []
		self.music_filenames = []
		self.playing = None
		self.tick = 0
		self.stop_at = 0
		self.shuffle = False
	
	# Load sounds
	def load_sound(self,name,format="ogg"):
		self.sounds[name] = pygame.mixer.Sound(os.path.join("res","audio",name+"."+format))
	
	# load music
	def load_music_from_ogg(self,name):
		snd = pygame.mixer.Sound(os.path.join("res","audio",name+".ogg"))
		snd.set_volume(0.5)
		self.music.append(snd)
		self.music_filenames.append(name)
	
	# Preload a piece of ogg-formatted music AFTER initialization
	def load_music(self,filename):
		if filename in self.music_filenames:
			return True
		self.load_music_from_ogg(filename)
		return True
	
	# Play a sound effect NOW
	def play(self,name):
		self.sounds[name].play()
	
	# Get soundtrack number by filename (w/out extension). 
	# Returns None if filename hasn't been loaded.
	def get_track_number(self,name):
		i = 0
		for f in self.music_filenames:
			if f == name:
				return i
			i += 1
		return None
	
	# Force the music to start, with an optional track number.
	def start_music(self,i=None):
		if i == None:
			i = random.randint(0,len(self.music)-1)
		if self.playing and False:
			self.playing.fadeout(1000)
		if i < 0 or i >= len(self.music):
			return False
		self.playing = self.music[i]
		self.playing.play()
		self.stop_at = time() + self.playing.get_length() + 1

	# Enables shuffling
	def shuffle(self,status=True):
		self.shuffle = status
	
	# Do music shuffle, if it's time for that and self.music_on is True
	def update(self):
		self.tick += 1
		if self.tick > 60:
			self.tick = 0
			if self.shuffle and not self.playing or time() > self.stop_at:
				self.playing = self.music[random.randint(0,len(self.music)-1)]
				self.playing.play()
				self.stop_at = time() + self.playing.get_length() + 1
