import os

def import_libs(dir):
		library_list = {} 
	
		for f in os.listdir(os.path.abspath(dir)):
			module_name, ext = os.path.splitext(f) # Handles no-extension files, etc.
			if ext == '.py': # Important, ignore .pyc/other files.
				print 'imported module: %s' % (module_name)
				module = __import__(module_name)
				library_list[module_name] = module
		return library_list

class State:
	__shared_state = {}
	
	def __init__(self):
		self.__dict__ = self.__shared_state
		
	def init_state(self):
		self.paused = False
		self.debug = False
		self.screen_size = (800,600)

	def pause(self,value=True):
		self.paused = value
