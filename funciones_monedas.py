import pygame

# Lista de monedas
monedas = [
    {"rect": pygame.Rect(220, 500, 30, 30), "recogida": False},  
    {"rect": pygame.Rect(220, 300, 30, 30), "recogida": False} ,
    {"rect": pygame.Rect(370, 200, 30, 30), "recogida": False},  
    {"rect": pygame.Rect(820, 100, 30, 30), "recogida": False}
] # las monedas del primer escenario

# Cargar el sprite de la moneda
sprite_moneda = pygame.transform.scale(pygame.image.load("assets/images/cristal_escenario_uno.png"), (100, 90))
