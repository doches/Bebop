import random
from State import State
import pygame
import math

class Particle:
	def __init__(self,coords,velocity,ttl,size=10):
		self.coords = [coords[0],coords[1]]
		self.velocity = [velocity[0],velocity[1]]
		self.ttl = ttl
		self.max_ttl = ttl
		self.size = size
		self.type = None
	
	def draw(self,surface):
		c = 255.0 * float(self.ttl) / self.max_ttl
		pygame.draw.circle(surface,(c,c,c),self.coords,self.size)
	
	def update(self):
		self.ttl -= 1
		if self.is_alive():
			self.coords[0] += self.velocity[0]
			self.coords[1] += self.velocity[1]
			
	def is_alive(self):
		return (self.ttl > 0)
		
class Source:
	def __init__(self,coords,max):
		self.particles = []
		self.max = max
		self.coords = [coords[0],coords[1]]
		self.ttl = 100
	
	def update(self):
		if len(self.particles) < self.max:
			for i in range(0,math.ceil((self.max+1.1)/self.ttl)):
				self.particles.append(self.spawn())
		dead_particles = []
		for particle in self.particles:
			particle.update()
			if particle.is_alive() == False:
				dead_particles.append(particle)
		for dead_particle in dead_particles:
			self.particles.remove(dead_particle)
		return True
	
	def spawn(self):
		return Particle(self.coords,((random.random()-0.5)*5,(random.random()-0.5)*5),self.ttl - random.randint(0,50))
	
	def draw(self,surface):
		for particle in self.particles:
			particle.draw(surface)

class Space:
	def __init__(self):
		self.sources = []
		self.effects = []
		self.obstacles = []
	
	def add_source(self,source):
		self.sources.append(source)
	
	def add_effect(self,effect):
		self.effects.append(effect)
	
	def add_obstacle(self,obstacle):
		self.obstacles.append(obstacle)
	
	def update(self):
		for source in self.sources:
			source.update()
		
		for effect in self.effects:
			effect.update()
		
		for obstacle in self.obstacles:
			obstacle.update()
		return True
	
	def draw(self,screen):	
		for obstacle in self.obstacles:
			obstacle.draw_shadow(screen)
		for obstacle in self.obstacles:
			obstacle.draw(screen)
		
		for source in self.sources:
			source.draw(screen)

		for effect in self.effects:
			effect.draw(screen)

Top = 1
Bottom = 2
Left = 4
Right = 8
class Obstacle:
	def __init__(self,source,coords,dims):
		self.source = source
		self.x = coords[0]
		self.y = coords[1]
		self.width = dims[0]
		self.height = dims[1]
	
	# Test to see if a particle is hitting this obstacle
	def hit_test(self,particle):	
		if particle.coords[0] > self.x - self.width/2 and particle.coords[0] < self.x + self.width/2:
			if abs(particle.coords[1] + particle.size - 2 - (self.y - self.height/2)) < abs(particle.velocity[1]): #Top
				return Top
			elif abs(particle.coords[1] - particle.size + 2 - (self.y + self.height/2)) < abs(particle.velocity[1]): # Bottom
				return Bottom
			else:
				return False
		elif particle.coords[1] > self.y - self.height/2 and particle.coords[1] < self.y + self.height/2:
			if abs(particle.coords[0] - (self.x - self.width/2)) < abs(particle.velocity[0]):
				return Left
			elif abs(particle.coords[0] - (self.x + self.width/2)) < abs(particle.velocity[0]):
				return Right
			else:
				return False
		else:
			return False
	
	def update(self,source=None):
		if source == None:
			source = self.source
		for particle in source.particles:
			retval = self.hit_test(particle)
			if retval != False:
				if retval == Top:
					particle.velocity = [particle.velocity[0],0]
				elif retval == Bottom:
					particle.velocity = [particle.velocity[0],1]
				elif retval == Right: 
					particle.velocity[0] = 1
				elif retval == Left:
					particle.velocity[0] = -1
	
	def draw(self,screen):
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(self.x-self.width/2,self.y-self.height/2,self.width,self.height))
		
	def draw_shadow(self,screen):
		pygame.draw.rect(screen,(128,128,128),pygame.Rect(self.x-self.width/2+2,self.y-self.height/2+2,self.width,self.height))
		
class Force:
	def __init__(self,source):
		self.source = source
	
	def update(self):
		for particle in self.source.particles:
			if self.in_effect(particle):
				self.effect(particle)
		return True
	
	def draw(self,surf):
		self
	
class Gravity(Force):
	def __init__(self,source,strength):
		Force.__init__(self,source)
		self.strength = strength
	
	def in_effect(self,particle):
		return True
	
	def effect(self,particle):
		particle.velocity[1] += self.strength

class Wind(Force):
	def __init__(self,source,strength,height,span):
		Force.__init__(self,source)
		self.strength = float(strength)
		self.height = height
		self.span = span
	
	def in_effect(self,particle):
		if particle.coords[1] > self.height - self.span and particle.coords[1] < self.height + self.span:
			return True
		return False
	
	def effect(self,particle):
		if(self.strength < 0 and particle.velocity[0] > self.strength):
			particle.velocity[0] -= 0.2
		elif(self.strength > 0 and particle.velocity[0] < self.strength):
			particle.velocity[0] += 0.2

class Reflect(Force):
	def in_effect(self,particle):
		screen = particle.state.screen_size
		if particle.coords[0] < 0 or particle.coords[0] > screen[0]:
			return True
	
	def effect(self,particle):
		particle.velocity[0] = -particle.velocity[0]/2

class ColoredParticle(Particle):
	def __init__(self,coords,velocity,ttl,size,color):
		Particle.__init__(self,coords,velocity,ttl,size)
		self.color = color
		self.state = State()
	
	def draw(self,surface):
		c = float(self.ttl) / self.max_ttl
		pygame.draw.circle(surface,(255-self.color[0] * c,255-self.color[1] * c,255-self.color[2]*c),self.coords,self.size)
	
	def is_alive(self):
		return (self.coords[1] < self.state.screen_size[1]+10) and self.ttl > 0
		
class InfiniteParticle(ColoredParticle):
	def __init__(self,coords,velocity,size,color):
		ColoredParticle.__init__(self,coords,velocity,255,size,color)
	
	def is_alive(self):
		return (self.coords[1] < self.state.screen_size[1]+10)
	
	def update(self):
		ColoredParticle.update(self)
		self.ttl += 1

class Fountain(Source):
		def spawn(self):
			return ColoredParticle(self.coords,((random.random()-0.5)*2,(random.random()-1)*10),random.randint(300,400),random.randint(2,4),(random.randint(196,255),random.randint(64,196),random.randint(0,64)))