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
velosidat=50
incremento_velocidad=0


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

	
def divuja_barra():
	pygame.draw.line(screen, black, (20, 550), (220, 550), 3)
	pygame.draw.line(screen, black, (20, 540), (20, 560), 3)
	pygame.draw.line(screen, black, (220, 540), (220, 560), 3)
	pygame.draw.line(screen, black, (70, 545), (70, 555), 2)
	pygame.draw.line(screen, black, (120, 545), (120, 555), 2)
	pygame.draw.line(screen, black, (170, 545), (170, 555), 2)
	pygame.draw.line(screen, red, (2*velosidat+20, 540), (2*velosidat+20, 560), 3)
	
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
pygame.font.init()
font = pygame.font.SysFont('Papyrus', 20)
font.set_bold(True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
try:
	icon=pygame.image.load("cannon.png")
	pygame.display.set_icon(icon)
except: print("icono no enctrado :(")
pygame.display.set_caption("Cannon")
finished = False
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: finished = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP: desfase = (pi/180)
			if event.key == pygame.K_DOWN: desfase = -(pi/180)
			if event.key == pygame.K_RIGHT: incremento_velocidad = 1
			if event.key == pygame.K_LEFT: incremento_velocidad = -1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN or event.key == pygame.K_UP: desfase = 0
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: incremento_velocidad = 0				
		
	if desfase > 0 and angulo+desfase > pi/2: angulo = pi/2
	elif desfase < 0 and angulo+desfase < 0: angulo = 0
	else: angulo+=desfase
	if incremento_velocidad < 0 and velosidat+incremento_velocidad >= 0 or incremento_velocidad > 0 and velosidat+incremento_velocidad <= 100: velosidat+=incremento_velocidad
	tangulo = font.render('ANGÚLO '+str(int(angulo*180/pi))+'°', False, (0, 0, 0))
	tevelosidat = font.render(str('VELOSIDAT '+str(velosidat)), False, (0, 0, 0))
	screen.fill(cyan)
	screen.fill(green, rect=[0,500,800,100])
	divuja_cannon()
	divuja_barra()
	screen.blit(tangulo,(10,10))
	screen.blit(tevelosidat,(10,40))
	pygame.display.update()
	clock.tick(fps)
	
pygame.quit()
quit()
 
