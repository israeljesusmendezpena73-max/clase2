import pygame
import sys
import random
import os
pygame.init()
x,y=3040,2160
window=pygame.display.set_mode((x,y))
pygame.display.set_caption("el robo equiva meteorito")
Fuente=pygame.font.Sysfont(arial,24)
fps=pygame.time.Clock
CIELO = (10,10,10)
BLANCO= (255,255,255)
ROJO=(220.60,60)
r_img=pygame.image.load(os.path.join("imagenes","robot.png")).convert_alpha
m_img=pygame.image.load(os.path.join("imagenes","meteorito.png")).convert_alpha
r_img=pygame.transform.scale(r_img,(60,60))
m_img=pygame.transform.scale(m_img,(40,40))
robot=pygame.Rect(x/2-30,y-80,60,60)
def jugar():
    robot=pygame.Rect(x/2-30,y-80,60,60)
    meteoritos=[]
    temnporadizador=0
    tem=40
    vm=5
    score=0
    run=True
    while run:
        reloj.tick(500)
        pantalla.fill(CIELO)
        for evento in pygame.event.get():
            if evento.type ==pygame.QUIT:
                corriendo=False
                keys=pygame.key.get_pressed
            if keys[pygame.K_RIGHT]:
                robot.x+=6
            if keys[pygame.K_LEFT]:
                robot.x-=6
            if robot.x<0:
                robot.x=0
            if robot.x>x-robot.width:
                robot.x=x-robot.width
                temnporadizador+=1
            if temnporadizador>tem:
                nuevo=pygame.Rect(random.randint(0,x,40),-40,40,40)
                meteoritos.append(nuevo)
                temnporadizador=0
            for m in meteorito:
                m.y+=vm
            antes=len[:]=[m for m in meteoritos if m.y>y]
            esquivados=antes-len[meteoritos]
            sore+=esquivados
            for m in meteoritos:
                if robot.collidedict(m):
                    run=False
            window.blit(r_img,(robot.x,robot.y))
            for m in meteoritos:
                window.blit(m_img,(m.x,m.y))
            txt=Fuente.render(f"puntos:{score}",True,BLANCO)
            pygame.display.flip()
            
pygame.quit()
sys.exit()