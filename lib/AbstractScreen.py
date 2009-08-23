import pygame

class AbstractScreen:
	# Create a new AbstractScreen. Don't do this, obviously.
	def __init__(self):
		self.previous = None
	
	# Call this when the screen is switched to. Can we make this automatic?
	def on_focus(self):
		raise Exception("Abstract on_focus() method called")
	
	# Draw this screen, returning True on success
	def draw(self,screen):
		return True
	
	# Return value:
	#	True -- successful update
	#	False -- Error in update OR done, and switch to previous screen
	def update(self):
		return True