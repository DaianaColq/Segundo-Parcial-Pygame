from configuracion import *
from personajes import *





def mover_personaje(personaje, rect_personaje, teclas, sprites):
    """Mueve al personaje y actualiza su posición en el rectángulo."""
    # Movimiento horizontal
    if teclas[pygame.K_LEFT] or teclas[pygame.K_RIGHT]:
        # Cambiar entre los dos sprites de correr
        if personaje.get("ultimo_cambio", 0) + 150 < pygame.time.get_ticks():  # Cambiar cada 150ms
            personaje["ultimo_cambio"] = pygame.time.get_ticks()
            # Alternar entre los dos sprites de correr
            if personaje["sprite actual"] == "corriendo_1":
                personaje["sprite actual"] = "corriendo_2"
            else:
                personaje["sprite actual"] = "corriendo_1"

        # Movimiento a la izquierda
        if teclas[pygame.K_LEFT]:
            rect_personaje.x -= personaje["velocidad x"]
            # Voltear el sprite horizontalmente cuando va a la izquierda
            '''sprite_volteado = pygame.transform.flip(sprites[personaje["sprite actual"]], True, False)
            sprites[personaje["sprite actual"]] = sprite_volteado'''
            if rect_personaje.left < 10:
                rect_personaje.left = 10
            

        # Movimiento a la derecha
        if teclas[pygame.K_RIGHT]:
            rect_personaje.x += personaje["velocidad x"]
            if rect_personaje.right > ANCHO -10:
                rect_personaje.right = ANCHO -10
            
    else:
        personaje["sprite actual"] = "inactivo"  # Si no se mueve, vuelve al sprite inactivo
        


    if teclas[pygame.K_SPACE] and personaje["en suelo"]:
        personaje["velocidad y"] = -personaje["fuerza salto"]  # Impulso hacia arriba
        personaje["en suelo"] = False
        personaje["sprite actual"] = "corriendo_1"

    

    


def aplicar_gravedad(personaje, rect_personaje, plataformas):
    """Aplica gravedad y verifica si el personaje toca el suelo."""
    if not personaje["en suelo"]:
        personaje["velocidad y"] += personaje["gravedad"]  # Aumenta la velocidad vertical

    rect_personaje.y += personaje["velocidad y"]  # Actualiza la posición en Y

    # Verificar colisión con las plataformas
    personaje["en suelo"] = False

    for plataforma in plataformas:
        if rect_personaje.colliderect(plataforma) and personaje["velocidad y"] > 0: # Solo si está cayendo
            if rect_personaje.bottom < plataforma.bottom : 
                # Coloca al personaje sobre la plataforma
                rect_personaje.bottom = plataforma.top
                personaje["en suelo"] = True
                personaje["velocidad y"] = 0  # Detener la caída
                break
    
    # Verifica colisión con el suelo
    if rect_personaje.bottom >= ALTO -50:  # un poco mas arriba del suelo para que quede bien esteticamente
        rect_personaje.bottom = ALTO -50
        personaje["en suelo"] = True
        personaje["velocidad y"] = 0  # Detener la caída

    # limitar caida por bugs
    if personaje["velocidad y"] > 15:
        personaje["velocidad y"] = 15