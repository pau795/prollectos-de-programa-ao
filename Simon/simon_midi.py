import sys, pygame, pygame.midi
from math import sin, cos, pi
from random import randint

res=[(640,480),(800,600),(1024,768)]

defres=1

WIDTH = res[defres][0]
HEIGHT = res[defres][1]
fullscreen=False
audio = True
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon")
pygame.midi.init()
player= pygame.midi.Output(pygame.midi.get_default_output_id())
player.set_instrument(46,1)

#Colores
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
green = (0,255,0)
brown = (133,87,35)
black = (0,0,0)
orange =(255,128,0)
white = (255,255,255)
blue2 = (0,128,192)


#fuentes
ftittle = pygame.font.SysFont('Papyrus', 30)
ftittle.set_bold(True)
stittle = pygame.font.SysFont('Papyrus', 25)
stittle.set_bold(True)
ftext = pygame.font.SysFont('Papyrus', 20)

#reloj
clock = pygame.time.Clock()
fps=60

def sum_alturas(l):
	suma=0
	for x in l:
		suma+=x.get_height()
	return suma


def cambiascreen():
	global WIDTH, HEIGHT
	WIDTH = res[defres][0]
	HEIGHT = res[defres][1]
	if (fullscreen):
		screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
	else:
		screen = pygame.display.set_mode((WIDTH, HEIGHT))
	
def escribe(l, ypos, p):
		i=0
		for x in l:
			m=x.get_height()
			xpost=int(WIDTH/2-x.get_width()/2)
			xpos=xpost-m/10
			screen.blit(x, (xpost,ypos))
			if i==p: pygame.draw.polygon(screen, red, [(xpos,ypos+m/2),(xpos-m/2*sin(45),ypos+3*m/4),(xpos-m/2*sin(45),ypos+m/4)],0)
			ypos+=m
			i+=1
			
def escribe_opciones(l, ypos, p):
		i=0
		for x in l:
			m=x.get_height()
			long=x.get_width()
			xpost=int(WIDTH/2-long/2)
			xpos=xpost-m/10
			xposd=int(WIDTH/2+long/2+m/10)
			screen.blit(x, (xpost,ypos))
			if i==p and p==4: pygame.draw.polygon(screen, red, [(xpos,ypos+m/2),(xpos-m/2*sin(45),ypos+3*m/4),(xpos-m/2*sin(45),ypos+m/4)],0)
			elif i==p:
				pygame.draw.polygon(screen, red, [(xpos, ypos+m/4),(xpos-m/2*sin(45),ypos+m/2),(xpos,ypos+3*m/4)],0)
				pygame.draw.polygon(screen, red, [(xposd,ypos+m/4),(xposd+m/2*sin(45),ypos+m/2),(xposd,ypos+3*m/4)],0)
			ypos+=m
			i+=1
		
def main_menu(p):
	tittle= ftittle.render('SIMON', False,red)
	if p==1: tutorial=ftext.render('Instructions', False, red)
	else: tutorial=ftext.render('Instructions', False, black)
	if p==2: new=ftext.render('New Game', False, red)
	else: new=ftext.render('New Game', False, black)
	if p==3: score=ftext.render('Top Scores', False, red)
	else: score=ftext.render('Top Scores', False, black)
	if p==4: settings=ftext.render('Settings', False, red)
	else: settings=ftext.render('Settings', False, black)
	if p==5: exit=ftext.render('Exit', False, red)
	else: exit=ftext.render('Exit', False, black)
	l=[tittle,tutorial,new,score,settings,exit]
	pos = int(HEIGHT/2-sum_alturas(l)/2)
	escribe(l, pos, p)

def onoff(b):
	if b: return 'On'
	else: return 'Off'
	
def menu_opciones(p):
	tittle= stittle.render('SETTINGS', False,red)
	if p==1: resolution=ftext.render('Resolution: '+str(WIDTH)+'x'+str(HEIGHT), False, red)
	else: resolution=ftext.render('Resolution: '+str(WIDTH)+'x'+str(HEIGHT), False, black)
	if p==2: fs=ftext.render('Full Screen: '+ str(fullscreen), False, red)
	else: fs=ftext.render('Full Screen: '+ str(fullscreen), False, black)
	if p==3: aud=ftext.render('Sound: '+ onoff(audio), False, red)
	else: aud=ftext.render('Sound: '+ onoff(audio), False, black)
	if p==4: back=ftext.render('Back', False, red)
	else: back=ftext.render('Back', False, black)
	l=[tittle,resolution,fs, aud,back]
	pos = int(HEIGHT/2-sum_alturas(l)/2)
	escribe_opciones(l, pos, p)
	
def scores():
	tittle= stittle.render('TOP SCORES', False,red)
	l=[tittle]	
	if len(topsc)==0:
		no_results=ftext.render('No scores available', False, black)
		l.append(no_results)
	else:
		i=0
		topsc.sort()
		for x in topsc[:5]:
			scorex=ftext.render('Score '+ str(i+1)+': '+str(x), False, black)
			l.append(scorex)
			i+=1
	back=ftext.render('Back', False, red)
	l.append(back)
	pos = int(HEIGHT/2-sum_alturas(l)/2)
	escribe(l,pos, len(l)-1)
	
	
def instrucciones():
	tittle= stittle.render('Instructions', False,red)
	inst1 = ftext.render('A pattern of lights and sounds is displayed.', False, black)
	inst2 = ftext.render('You have to use the arrow keys to repeat the pattern.', False, black)
	inst3 = ftext.render('Afterwards, the pattern is increased by one step.', False, black)
	inst4 = ftext.render('How many steps are you able to remember?', False, black)
	
	back=ftext.render('Back', False, red)
	l=[tittle,inst1,inst2,inst3,inst4,back]
	pos = int(HEIGHT/2-sum_alturas(l)/2)
	escribe(l,pos, len(l)-1)
	
def new_game():
	start= ftext.render('Press Return to start...', False,black)
	l=[start]
	pos = int(HEIGHT-sum_alturas(l))
	escribe(l,pos, 0)	
	
def colors(p):
	if p==1:
		colorUP=(92,255,128)
		borderUP=(0,199,0)
	else:
		colorUP=green
		borderUP=black
	if p==2:
		colorLEFT=(255,92,92)
		borderLEFT=(199,0,0)
	else:
		colorLEFT=red
		borderLEFT=black
	if p==3:
		colorDOWN=(92,92,255)
		borderDOWN=(0,0,199)
	else:
		colorDOWN=blue
		borderDOWN=black
	if p==4:
		colorRIGHT=(255,255,128)
		borderRIGHT=(199,199,0)
	else:
		colorRIGHT=yellow
		borderRIGHT=black
	return colorUP, colorDOWN,colorLEFT,colorRIGHT, borderUP, borderDOWN, borderLEFT, borderRIGHT
	
def simon(b):
	center=(int(WIDTH/2), int(HEIGHT/2))
	radio=int(HEIGHT/5)
	colorUP, colorDOWN,colorLEFT,colorRIGHT, borderUP, borderDOWN, borderLEFT, borderRIGHT = colors(b)
	pygame.draw.circle(screen, orange, center,radio, 0)
	pygame.draw.rect(screen, colorUP, [center[0]-radio,center[1]-2*radio,2*radio, radio/2], 0)
	pygame.draw.rect(screen, colorLEFT, [center[0]-2*radio,center[1]-radio,radio/2, 2*radio], 0)
	pygame.draw.rect(screen, colorDOWN, [center[0]-radio,center[1]+1.5*radio,2*radio, radio/2], 0)	
	pygame.draw.rect(screen, colorRIGHT, [center[0]+1.5*radio,center[1]-radio,radio/2, 2*radio], 0)
	pygame.draw.circle(screen, black, center,radio, 1)
	pygame.draw.rect(screen, borderUP, [center[0]-radio,center[1]-2*radio,2*radio, radio/2], 1)
	pygame.draw.rect(screen, borderLEFT, [center[0]-2*radio,center[1]-radio,radio/2, 2*radio], 1)
	pygame.draw.rect(screen, borderDOWN, [center[0]-radio,center[1]+1.5*radio,2*radio, radio/2], 1)	
	pygame.draw.rect(screen, borderRIGHT, [center[0]+1.5*radio,center[1]-radio,radio/2, 2*radio], 1)
	tittle= ftittle.render('SIMON', False,black)
	screen.blit(tittle, (center[0]-tittle.get_width()/2,center[1]-tittle.get_height()/2))
	score= ftext.render('Score: '+str(sc), False,black)
	screen.blit(score, (0,HEIGHT-score.get_height()))
	
def turno(b):
	global sc, estado, display, turn, stack, pos_stack
	if turn:
		if(change ==1 and b != 0):
			if pos_stack < len(stack):
				if stack[pos_stack]!=b:
					simon(stack[pos_stack])
					pygame.display.update()
					player.set_instrument(40,1)
					if audio: player.note_on(35, 127,1)
					pygame.time.delay(1000)
					if audio: player.note_off(35, 127,1)
					player.set_instrument(46,1)
					estado = 2
					topsc.append(sc)
					sc=0
					turn = False
					display = False
					stack = []
					pos_stack=0
				elif pos_stack==len(stack)-1:
					pygame.time.delay(500)
					simon(0)
					pygame.display.update()
					pygame.time.delay(1000)
					sc+=1
					turn=False
					display=False
					pos_stack=0
				else: pos_stack+=1
	elif not display:
		stack.append(randint(1,4))
		pos_stack=0
		display=True;
		
def note1(button):
	if button==1: return 50
	if button==2: return 60
	if button==3: return 70
	if button==4: return 80
	
estado=0
finished = False
opcion_menu=2
opcion_settings=1
topsc=[]
stack=[]
button=0
sc=0
note=0
change=0
display=False
turn=False
pos_stack=0;
pressed=False
while not finished:
	screen.fill(blue2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: finished = True
	if estado==0: #menu principal
		main_menu(opcion_menu)
		if event.type == pygame.KEYDOWN:
			if not pressed and event.key == pygame.K_UP:
				if opcion_menu > 1:
					opcion_menu-=1
					pressed=True				
			if not pressed and event.key == pygame.K_DOWN:
				if opcion_menu < 5: 
					opcion_menu+=1
					pressed=True
			if not pressed and event.key == pygame.K_RETURN:
				estado=opcion_menu
				pressed=True
			if not pressed and event.key == pygame.K_ESCAPE: 
				opcion_menu=5
				pressed=True
	if estado==1: #instrucciones
		instrucciones()
		if event.type == pygame.KEYDOWN:
			if not pressed and event.key == pygame.K_RETURN:
				estado=0
				pressed=True
	if estado==2: #inicio partida
		simon(0)
		new_game()
		if event.type == pygame.KEYDOWN:
			if not pressed and event.key == pygame.K_RETURN:
					estado=6
					pressed=True
			if not pressed and event.key == pygame.K_ESCAPE: 
					estado=0
					pressed=True
	if estado==3: #puntuacion
		scores()
		if event.type == pygame.KEYDOWN:
			if not pressed and event.key == pygame.K_RETURN:
				estado=0
				pressed=True
	if estado==4: #opciones
		menu_opciones(opcion_settings)
		if event.type == pygame.KEYDOWN:
			if not pressed and event.key == pygame.K_UP:
				if opcion_settings > 1:
					opcion_settings-=1
					pressed=True				
			if not pressed and event.key == pygame.K_DOWN:
				if opcion_settings < 4: 
					opcion_settings+=1
					pressed=True	
			if not pressed and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
				if opcion_settings==1:
					if event.key == pygame.K_LEFT:
						if defres==0: defres=len(res)-1
						else: defres-=1
					if event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN: 
						if defres==len(res)-1: defres=0
						else: defres+=1
					cambiascreen()
				elif opcion_settings==2:
					fullscreen = not fullscreen
					cambiascreen()
				elif opcion_settings==3:
					audio= not audio
				pressed=True
			if not pressed and event.key == pygame.K_ESCAPE: 
				opcion_menu=2
				estado=0
				pressed=True
			if not pressed and event.key == pygame.K_RETURN:
				if opcion_settings==4:
					opcion_settings=2
					estado=0
				pressed=True
	if event.type == pygame.KEYUP: 
			pressed=False
	if estado==5: finished = True
	if estado==6: #juego
		simon(button)
		pygame.display.update()
		turno(button)
		if display:
			if pos_stack < len(stack):
				button=stack[pos_stack]
				simon(button)
				pygame.display.update()
				if audio: player.note_on(note1(button),127,1)
				pygame.time.delay(700)
				if audio: player.note_off(note1(button),127,1)
				simon(0)
				pygame.display.update()
				pygame.time.delay(300)
				pos_stack+=1
			else:
				pos_stack=0
				button=0
				display=False
				turn=True
		if turn and event.type == pygame.KEYDOWN:
			if not pressed:
				if event.key == pygame.K_UP:
					button=1
					change+=1
					note=note1(button)
					pressed=True
					if audio: player.note_on(note, 127,1)
				if event.key == pygame.K_LEFT:
					button=2
					change+=1
					note=note1(button)
					pressed=True	
					if audio: player.note_on(note, 127,1)
				if event.key == pygame.K_DOWN:
					button=3
					change+=1
					note=note1(button)
					pressed=True		
					if audio: player.note_on(note, 127,1)
				if event.key == pygame.K_RIGHT:
					button=4
					change+=1
					note=note1(button)
					pressed=True
					if audio: player.note_on(note, 127,1)
			else: change+=1
			if not pressed and event.key == pygame.K_ESCAPE:
				estado=0
				sc=0
				stack = []
				pos_stack=0
				turn=False
				display=False
				pressed=True
		if turn and event.type == pygame.KEYUP: 
			pressed=False
			change=0
			button=0
			if audio and note!=0: player.note_off(note, 127,1)
			note=0
	pygame.display.update()
	clock.tick(fps)
pygame.quit()
player.close()
quit()