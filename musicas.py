import pygame

pygame.init()
pygame.mixer.init()

def musica_normal():
    pygame.mixer.music.load("ambiente.mp3")
    pygame.mixer.music.play(-1)  # loop infinito

def musica_batalha():
    pygame.mixer.music.load("batalha.mp3")
    pygame.mixer.music.play(-1)

def parar_musica():
    pygame.mixer.music.stop()

# começa com música normal
