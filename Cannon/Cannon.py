import sys, pygame
from pygame.locals import *
from math import cos, sin, pi
 

WIDTH = 800
HEIGHT = 600

red = (255,0,0)
cyan =(0,255,255)
green = (0,255,0)
brown = (133,87,35)
black = (0,0,0)

longitud_cannon= 80
ancho_cannon= 20

centro = (35,475)
radio = 15
angulo=(pi)


def cannon(l,possissao, radio, arfa):
	vsi= (possissao[0]+radio*cos((3*pi/4)-arfa),possissao[1]+radio*sin((3*pi/4)-arfa))
	vsd= (vsi[0]+l*cos(arfa), vsi[1]+l*sin(-arfa))
	vii= (possissao[0]+radio*cos((5*pi/4)-arfa),possissao[1]+radio*sin((5*pi/4)-arfa))
	vid=(vii[0]+l*cos(arfa), vii[1]+l*sin(-arfa))
	return [vsi,vii,vid,vsd]


def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("LOL")
	finished = False
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True
				
		screen.fill(cyan)
		screen.fill(green, rect=[0,500,800,100])
		screen.fill(brown, rect=[20,480,50,20])
		pygame.draw.circle(screen, black,centro, radio, 0)
		pygame.draw.polygon(screen, black, cannon(longitud_cannon, centro, radio, angulo),0)
		pygame.display.update()
	
	pygame.quit()
	quit()
	return 0
 
if __name__ == '__main__':
    pygame.init()
    main()