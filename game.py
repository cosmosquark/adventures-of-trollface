import pygame, sys, os
import time
import random
import numpy
import mainmenu


def main():
   running = True
   location = 'main menu'
   pygame.init()
   screen = pygame.display.set_mode((800,600))
   pygame.display.set_caption("TROLOLOLOLOLOLOLOLOLOLOLOL")
   screen.fill((255,255,255))
   while running:
      if location == 'main menu':
         while location == 'main menu':
            location = mainmenu.main(location, screen)
            if location != 'main menu':
               break
      if location == 'char':
         while location == 'char':
            import char
            location = char.main(location, screen)
            if location != 'char':
               break

      for event in pygame.event.get():
      # only do something if the event is of type QUIT
         if event.type == pygame.QUIT:
         # change the value to False, to exit the main loop
            running = False
            sys.exit()


if __name__=="__main__":
    # call the main function
    main()
