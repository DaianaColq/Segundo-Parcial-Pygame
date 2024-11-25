import pygame
from configuracion import *
from personajes import *
from funciones_movimientos import *
from menu import *
from plataformas_primer_escenario import *
from funciones_dibujar import *

def primer_escenario(ventana,protagonista, sprites, rect_personaje):
    reloj = pygame.time.Clock()
    jugando = True
    

    while jugando:

        ventana.blit(FONDO_UNO, (0, 0))  # Fondo del escenario
        

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #sale del juego
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Si presiona ESC, regresa al menú
                    return "menu"
                

        
        
        
        teclas = pygame.key.get_pressed()
        #mover_personaje(protagonista, rect_personaje, teclas, sprites)
        aplicar_gravedad(protagonista, rect_personaje, plataformas)
        dibujar_plataformas(ventana, plataformas, sprite_plataforma)

        mover_personaje(protagonista, rect_personaje, teclas, sprites)
        '''ventana.blit(sprites[protagonista["sprite actual"]], rect_personaje)  # Dibujar el sprite actual'''
        # Obtener el sprite actual
        sprite_personaje = sprites[protagonista["sprite actual"]]

        # Si el personaje va a la izquierda, lo volteamos (flip)
        if teclas[pygame.K_LEFT]:
            sprite_personaje = pygame.transform.flip(sprite_personaje, True, False)
        dibujar_enemigos(ventana, enemigos, rects_enemigos, sprites_enemigos)
        # Dibujar el sprite en la pantalla
        ventana.blit(sprite_personaje, rect_personaje)
        pygame.display.flip()
        reloj.tick(60)