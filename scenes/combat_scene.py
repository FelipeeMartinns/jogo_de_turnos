import pygame

def draw_bar(screen, x, y, w, h, current, max_value):
    ratio = current / max_value
    pygame.draw.rect(screen, (255,0,0), (x,y,w,h))
    pygame.draw.rect(screen, (0,255,0), (x,y,w*ratio,h))

def combat_scene(screen, player, enemy):
    screen.fill((30,30,30))

    draw_bar(screen, 50, 50, 200, 20, player.life, player.max_life)
    draw_bar(screen, 550, 50, 200, 20, enemy.life, enemy.max_life)

    font = pygame.font.SysFont(None, 30)
    txt = font.render("Pressione A para atacar", True, (255,255,255))
    screen.blit(txt, (250, 500))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        enemy.life -= max(player.damage_ad - enemy.damage_ad, 1)
