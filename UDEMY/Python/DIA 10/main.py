import pygame
import random
import math
from pygame import mixer


#Inicializar pygame
pygame.init()

#CREAR PANTALLA
pantalla = pygame.display.set_mode((800, 600))

#TITULO E ICONO
pygame.display.set_caption("Nos invaden los marcianos")
icono = pygame.image.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\ovni.ico")
pygame.display.set_icon(icono)
fondo = pygame.image.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\Fondo.jpg")

#AGREGAR MUSICA
mixer.music.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\MusicaFondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)




#JUGADOR VARIABLES
img_jugador = pygame.image.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\jugador.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#ENEMIGO VARIABLES
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = [] 
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.1)
    enemigo_y_cambio.append(50)

#BALA VARIABLES
img_bala = pygame.image.load("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#FUNCION DISPARAR BALA
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#TEXTO FINAL DEL  JUEGO
fuente_final = pygame.font.Font("freesansbold.ttf", 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


#PUNTAJE    
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

#FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#JUGADOR  FUNCION
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

#enemigo  FUNCION
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#FUNCION DETECTAR COLISIONES
def hay_colicion(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


#LOOP JUEGO
se_ejecuta = True
while se_ejecuta:
    #IMAGEN DE FONDO    
    pantalla.blit(fondo, (0, 0))

    #SALIR DEL JUEGO
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #PRESIONAR FLECHAS MOVIMIENTO
        if evento.type == pygame.KEYDOWN:   
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.2
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\disparo.mp3")
                sonido_bala.play()
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #SOLTAR FLECHAS
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
        
        
        

    #MODIFICAR UBICACION DEL JUGADOR
    jugador_x += jugador_x_cambio

    #MANTENER DENTRO DEL BORDE JUGADOR
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 750:
        jugador_x = 750

    #MODIFICAR UBICACION DEL ENEMIGO
    for e in range(cantidad_enemigos):

        #FIN DEL JUEGO
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        #MANTENER DENTRO DEL BORDE ENEMIGO
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        #COLISION
        colision = hay_colicion(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("C:\\Users\\Damia\\Desktop\\Estudios\\Python\\segunda prueba\\DIA 10\\Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)

    #MOVIMIENTO BALA
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

  


    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    #ACTUALIZAR
    pygame.display.update()