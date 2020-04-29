import sys, pygame
from math import cos, sin, pi
 
class Vola:
    def __init__(self, radeo, posiçao, veloçao):
        self.radeo = int(radeo)
        self.posiçao = posiçao
        self.veloçao = veloçao
        self.ndim = 2

    def buela_un_poquete(self, dt):
        """MUEBE UN POCO LA VOLA."""
        for i in range(self.ndim):
            self.veloçao[i] += f[i]*dt
            self.posiçao[i] += self.veloçao[i]*dt

    def divuja_vola(self, screen):
        # TODO: Divuga vola
        posiçao = [int(i) for i in self.posiçao]
        pygame.draw.circle(screen, black, posiçao, self.radeo, 0)
        
#bentana
WIDTH = 800
HEIGHT = 600

#colores
red = (255,0,0)
cyan =(0,255,255)
green = (0,255,0)
brown = (133,87,35)
black = (0,0,0)

#medidas
ancho_suelo =int(HEIGHT/6)
inicio_suelo = HEIGHT-ancho_suelo
margen=int(WIDTH/40)

#cannon en si, incongoscible
radio = margen+0
centro = (margen+radio,int(inicio_suelo-1.5*radio))
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
    centro = inicio_suelo + ancho_suelo/2
    l = WIDTH/4
    m=margen
    g=ancho_suelo/10
    p=g/2
    
    pygame.draw.line(screen, black, (m, centro), (m+l, centro), 3) #linea horizontal
    pygame.draw.line(screen, black, (m, centro-g), (m, centro+g), 3) #linea vertical izq
    pygame.draw.line(screen, black, (m+l, centro-g), (m+l, centro+g), 3) #linea vertical der
    pygame.draw.line(screen, black, (m+l/4, centro-p), (m+l/4,centro+p ), 2) #separador vertical izq
    pygame.draw.line(screen, black, (m+l/2, centro-p), (m+l/2, centro+p), 2) #separador vertical centr
    pygame.draw.line(screen, black, (m+l*3/4, centro-p), (m+l*3/4, centro+p), 2) #separador vertical der
    pygame.draw.line(screen, red, (l/100*velosidat+margen, centro-g), (l/100*velosidat+margen, centro+g), 3)
    ti1 =  font.render('0', False, (0, 0, 0))
    ti2 =  font.render('100', False, (0, 0, 0))
    screen.blit(ti1,(g+p, centro+g))
    screen.blit(ti2,(l, centro+g))
    
def divuja_fondo():
    screen.fill(cyan)
    screen.fill(green, rect=[0,inicio_suelo,WIDTH,ancho_suelo])
    
def escrive_testo():
    tangulo = font.render('ANGÚLO '+str(int(angulo*180/pi))+'°', False, (0, 0, 0))
    tevelosidat = font.render(str('VELOSIDAT '+str(int(velosidat))), False, (0, 0, 0))
    screen.blit(tangulo,(int(margen/2),int(margen/2)))
    screen.blit(tevelosidat,(int(margen/2),2*margen))


#reloj
clock = pygame.time.Clock()
fps=60

#mobimiento

g = 500
x0 = 100
v0 = 0
dt = 1/fps

def euler(f, v0, x0, h):
    return v0+f(x0, v0)*h


f = [0, g]

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
font = pygame.font.SysFont('Papyrus', int(margen))
font.set_bold(True)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
try:
    icon=pygame.image.load("cannon.png")
    pygame.display.set_icon(icon)
except: print("icono no enctrado :(")
pygame.display.set_caption("Cannon")
ecsiste_vola = False
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: desfase = (pi/180)
            if event.key == pygame.K_DOWN: desfase = -(pi/180)
            if event.key == pygame.K_RIGHT: incremento_velocidad = 1
            if event.key == pygame.K_LEFT: incremento_velocidad = -1
            if event.key == pygame.K_SPACE:
                angulo_correcto = -angulo
                vola = Vola(radio*.7, list(centro), [10*velosidat*cos(angulo_correcto), 
                    10*velosidat*sin(angulo_correcto)])
                ecsiste_vola = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP: desfase = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT: incremento_velocidad = 0                
        
    # Jirar el CANNON
    if desfase > 0 and angulo+desfase > pi/2: angulo = pi/2
    elif desfase < 0 and angulo+desfase < 0: angulo = 0
    else: angulo+=desfase
    if incremento_velocidad < 0 and velosidat+incremento_velocidad >= 0 or incremento_velocidad > 0 and velosidat+incremento_velocidad <= 100: velosidat+=incremento_velocidad
    escrive_testo()
    divuja_fondo()
    divuja_cannon()
    divuja_barra()
    if ecsiste_vola: 
        vola.buela_un_poquete(dt)
        vola.divuja_vola(screen)
        if vola.posiçao[1] > inicio_suelo:
            ecsiste_vola = False
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()
