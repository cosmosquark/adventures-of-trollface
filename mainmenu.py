import pygame, sys, os
import random

def main(location, screen):
   running = True
   while running:
      # event handling, gets all event from the eventqueue
      screen.fill((255,255,255))
      image = pygame.image.load("trollface.jpg")
      screen.blit(image, (random.randint(0,555),random.randint(0,255))) #places image at this co-ordinates
      newgame = pygame.image.load("NG.gif")
      screen.blit(newgame, (300,400))
      pygame.display.flip() #moves the image on top of the background
      pygame.time.wait(200)
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
               running = False
               location = 'char'
               return location
      if event.type == pygame.QUIT:
         # change the value to False, to exit the main loop
         running = False
         sys.exit()

