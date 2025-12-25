import pygame
import sys

from core.charactere import Charactere
from core.enemy import Enemy
from core.combat import Combat
from core.items import Items

from scenes.menu_scene import menu_scene
from scenes.combat_scene import combat_scene
from scenes.shop_scene import shop_scene


# ===== INIT =====
pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("RPG")

clock = pygame.time.Clock()

# ===== ESTADO DO JOGO =====
state = "menu"

# ===== ENTIDADES =====
player = Charactere("Felipe")
enemy = Enemy("Slime")
combat = Combat()
items = Items()


# ===== LOOP PRINCIPAL =====
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== MENU =====
        if state == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state = "combat"
            elif event.key == pygame.K_s:   # abrir loja
                state = "shop"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # ===== COMBATE =====
        if state == "combat" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                combat.attack(player, enemy)
            elif event.key == pygame.K_ESCAPE:
                state = "menu"

        # ===== LOJA =====
        if state == "shop" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                items.buy_sword(player)
            elif event.key == pygame.K_2:
                items.buy_staff(player)
            elif event.key == pygame.K_3:
                items.buy_armor(player)
            elif event.key == pygame.K_ESCAPE:
                state = "menu"

    # ===== DESENHO DAS CENAS =====
    if state == "menu":
        menu_scene(SCREEN)

    elif state == "combat":
        combat_scene(SCREEN, player, enemy)

    elif state == "shop":
        shop_scene(SCREEN, player, items)

    pygame.display.flip()
    clock.tick(60)
