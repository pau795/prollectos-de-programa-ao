import sys, pygame
from math import cos, sin, pi
 
#bentana
WIDTH = 800
HEIGHT = 600

#colores
red = (255,0,0)
cyan =(0,255,255)
green = (0,255,0)
brown = (133,87,35)
black = (0,0,0)

#cannon en si, incongoscible
radio = 20
centro = (20+radio,int(500-1.5*radio))
angulo=0
desfase=0
longitud_cannon= 5*radio

def cannon(l,possissao, radio, arfa):
	vsi= (possissao[0]+radio*cos((3*pi/4)-arfa),possissao[1]+radio*sin((3*pi/4)-arfa))
	vsd= (vsi[0]+l*cos(arfa), vsi[1]+l*sin(-arfa))
	vii= (possissao[0]+radio*cos((5*pi/4)-arfa),possissao[1]+radio*sin((5*pi/4)-arfa))
	vid=(vii[0]+l*cos(arfa), vii[1]+l*sin(-arfa))
	return [vsi,vii,vid,vsd]

def divuja_cannon():
	pygame.draw.rect(screen, brown,[centro[0]-radio,centro[1],3*radio,1.5*radio])
	pygame.draw.circle(screen, black,centro, radio, 0)
	pygame.draw.polygon(screen, black, cannon(longitud_cannon, centro, radio, angulo),0)

#reloj
clock = pygame.time.Clock()
fps=60

#mobimiento

g = 9.807
x0 = 100
v0 = 0
h = 1/fps

def euler(f, v0, x0, h):
    return v0+f(x0, v0)*h

f = lambda x, v: -g

def trallecto(f, x0, v0, h):
    v = euler(f,v0,x0,h)
    x = x0+v*h
    return x, v

"""
for i in range(100):
    x, y = trallecto(f,x0,v0,h)
    x0 = x
    v0 = y
	print(x, y)
"""

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LOL")
finished = False
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				desfase = (pi/180)
			if event.key == pygame.K_DOWN:
				desfase = -(pi/180)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				desfase = 0		
		
	if desfase < 0 and angulo > 0 or desfase > 0 and angulo < (pi/2): angulo+=desfase
	screen.fill(cyan)
	screen.fill(green, rect=[0,500,800,100])
	divuja_cannon()
	pygame.display.update()
	clock.tick(fps)
	
pygame.quit()
quit()
 
