import pygame

pygame.init()
pygame.mixer.init()

def musica_normal():
    pygame.mixer.music.load("ambiente.mp3")
    pygame.mixer.music.play(-1)  # loop infinito

def musica_batalha():
    pygame.mixer.music.load("batalha.mp3")
    pygame.mixer.music.set_volume(0.8)
    
    pygame.mixer.music.play(-1)

def musica_morreu():
    pygame.mixer.music.load("morreu.mp3")
    pygame.mixer.music.play(-1)

def parar_musica():
    pygame.mixer.music.stop()

# começa com música normal


som_dano = pygame.mixer.Sound("atak.mp3")
som_compra = pygame.mixer.Sound("bloup.mp3")
som_clik= pygame.mixer.Sound("clik.mp3")
som_defesa= pygame.mixer.Sound("defesa.mp3")
som_errou= pygame.mixer.Sound("errou.mp3")
som_vitoria= pygame.mixer.Sound("vitoria.mp3")
