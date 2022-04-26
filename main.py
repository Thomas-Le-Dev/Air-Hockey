import pygame
import sys

pygame.init()

screen_largeur, screen_hauteur = 1000, 500

screen = pygame.display.set_mode((screen_largeur, screen_hauteur))
my_surface = pygame.Surface((100, 100))

#my_rect1 = pygame.Rect(50, 75, 125, 125)
my_rect2 = pygame.Rect(75, 100, 150, 150)

x_speed, y_speed = 1, 1

timer = pygame.time.Clock()
x1 = 0
y1 = 125

x2 = 800
y2 = 125

x3 = 250
y3 = 125


def balle_collision():
    global x_speed, y_speed
    rectBalle.x += x_speed
    rectBalle.y += y_speed
    #Collision de la balle avec les bordures de l'écran

    if rectBalle.right >= screen_largeur or rectBalle.left <= 0:
        x_speed *= -1
    if rectBalle.bottom >= screen_hauteur or rectBalle.top <= 0:
        y_speed *= -1

    #Collision de la balle avec les joueurs

    Tolerance_collision = 10
    if rectBalle.colliderect(hitbox_joueur1):
        #Utiliser la valeur absolue pour que les soustraction avec un resultat négatif ne créé pas de bug
        if abs(hitbox_joueur1.top - rectBalle.bottom) == Tolerance_collision and y_speed > 0:
            y_speed *= -1
        if abs(hitbox_joueur1.bottom - rectBalle.top) == Tolerance_collision and y_speed < 0:
            y_speed *= -1
        if abs(hitbox_joueur1.right - rectBalle.left) == Tolerance_collision and x_speed < 0:
            x_speed *= -1
        if abs(hitbox_joueur1.left - rectBalle.right) == Tolerance_collision and x_speed > 0:
            x_speed *= -1

    #Si on draw le rect il est normal de pas voir l'image s'afficher
    #pygame.draw.rect(screen, (255, 255, 255), rectBalle)

game_on = True

terrain = pygame.image.load("terrain_airhockey.png")
joueur1 = pygame.image.load("Air_Hockey_Player1.png").convert_alpha()
joueur2 = pygame.image.load("Air_Hockey_Player2.png").convert_alpha()
balle = pygame.image.load("Air_Hockey_Ball.png").convert_alpha()

rectBalle = balle.get_rect()
rectBalle.topleft = (500,250)

hitbox_joueur1 = joueur1.get_rect()
#hitbox_joueur1.topleft = (150, 250)

hitbox_joueur2 = joueur2.get_rect()
hitbox_joueur2.topleft = (850, 250)

#image3 = pygame.image.load("joueur1.png").convert()
#image3 = pygame.image.load("palais2.jpg")
#joueur1 = joueur1.convert_alpha()
#joueur2 = joueur2.convert_alpha()
#image3 = image3.convert_alpha()

while game_on:
    #Coordonnés pour 2ème joueur avec souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed1 = pygame.key.get_pressed()
    if pressed1[pygame.K_d]:
        x1 += 1
    if pressed1[pygame.K_q]:
        x1 -= 1
    if pressed1[pygame.K_z]:
        y1 -= 1
    if pressed1[pygame.K_s]:
        y1 += 1
    

    #Code pour 2 eme joueur avec touches
    """
    pressed2 = pygame.key.get_pressed()
    if pressed2[pygame.K_RIGHT]:
        x2 += 1
    if pressed2[pygame.K_LEFT]:
        x2 -= 1
    if pressed2[pygame.K_UP]:
        y2 -= 1
    if pressed2[pygame.K_DOWN]:
        y2 += 1
    """
    

    
    screen.blit(terrain, (0, 0))
    #screen.fill(pygame.Color("black"))
    #my_surface.fill((35, 237, 219))
    #screen.blit(my_surface, (x, y))
    screen.blit(joueur1, (x1, y1))
    screen.blit(joueur2, (mouse_x - 50, mouse_y - 50))
    screen.blit(balle, rectBalle)
    #screen.blit(image3, (x3, y3))
    
    
    balle_collision()

    #rectBalle = pygame.Rect(350, 350, 100, 100)


    #pygame.draw.rect(screen, pygame.Color("purple"), my_rect)
    #print(f"x = {x} et y = {y}")
    pygame.display.update()

    


    
    #x += 1
    #y -= 1
    #my_rect.right += 1
    timer.tick(400)