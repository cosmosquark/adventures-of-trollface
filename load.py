import pygame

def loadscreen(screen):
   screen.fill((0,0,0))
   loadscreen = pygame.image.load('loadingscreen/1297452511251.jpg').convert()
   screen.blit(loadscreen, (10, 10),)
   pygame.display.flip()
