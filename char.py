import pygame, sys, os
import time
import random
import numpy
import scipy
import loaddata
import load
import charmoveandcollision as charcheck

# define character and also intialise starting location
class char:
   image = pygame.image.load('trolltest.png').convert()
   x = 40 # location on the screen
   y = 10
   vx = 0 # velocity
   vy = 0
   placeX = 40
   placeY = 30


#   def jump:
#   def moveleft:
#   def moveright:
#   def fall:
#   def update:


def main(location, screen):
   load.loadscreen(screen)
   screen.fill((0,0,0))
   loadscreen = pygame.image.load('loadingscreen/1297452511251.jpg').convert()
   screen.blit(loadscreen, (10, 10),)
   pygame.display.flip()
   timeloadstart = pygame.time.get_ticks()
   
   sf = 10 #conversion from 80 x 80 array to screen location
   pygame.HWSURFACE
   shell = numpy.zeros((60,80))
   level = loaddata.loadlevel("demolevel.png")
   floor = pygame.image.load('black5.png').convert()
 
   screenresolutionX = 800
   screenresolutionY = 600
   
   gameresX = screenresolutionX / sf
   gameresY = screenresolutionY / sf

   halfresX = gameresX / 2
   halfresY = gameresY / 2

   #level loader
   for el in level:
      arra = []
      for foo in el:
         if not foo:
            arra.append(" ")
         else:
            arra.append(float(foo))
   divzero = 1/10
   totalX = level.shape[1]
   totalY = level.shape[0]
   
   #set the loading time so user can see image.
   timeloadfinish = timeloadstart + 4000
   while timeloadstart < timeloadfinish:
      timeloadstart = pygame.time.get_ticks()
      if timeloadstart > timeloadfinish:
          break
      pygame.time.wait(500)
   
   screen.fill((255,255,255))

   # define the initial start location, velocity and conditions
   char.x = 20
   char.y = 4
   char.vx = 0
   char.vy = 0
   shell = level[char.placeY - halfresY :char.placeY + halfresY,char.placeX - halfresX:char.placeX + halfresX]
   level[char.y: char.y + 10, char.x: char.x + 5] = 2
   
   left = False
   leftcounter = 0
   right = False
   rightcounter = 0
   walk = True
   jump = False
   jumping = False
   falling = False
   fallcounter = 0
   jumpcounter = 0
   doublejumpcounter = 0
   lolcount = 0

   for y in range(0,gameresY):
      for x in range(0, gameresX):
         if 3 == shell[y,x]:
            screen.blit(floor, (x * 10, y * 10),) 
   pygame.display.flip()
   running = True

   while running:
      pygame.time.wait(10)
      # obtain all the objects etc to place on the screen
      char.placeX, char.placeY = charcheck.charlocation(char.x, char.y, totalX, totalY, halfresX, halfresY)
      # create the screen (or shell)
      shell = level[char.placeY - halfresY:char.placeY + halfresY, char.placeX- halfresX: char.placeX + halfresX]
      screen.fill((255,255,255))
      charfound = False
      for y in range(0,gameresY):
         for x in range(0,gameresX):
            if 3 == shell[y,x]:
               screen.blit(floor, (x * sf, y * sf),)
            if 2 == shell[y,x] and charfound == False:
               screen.blit(char.image, (x * sf, y * sf))
               charfound = True
      pygame.display.flip()

      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              if jump == True:
                 if doublejumpcounter <= 1:
                   jumping = True
                   doublejumpcounter = doublejumpcounter + 1
                   jumpcounter = 0
                   falling = False
                 elif doublejumpcounter >= 2:
                   jump = False
                   doublejumpcounter = 0
            if event.key == pygame.K_LSHIFT:
               walk = False
               if event.key == pygame.K_RIGHT:
                 right = True
               elif event.key == pygame.K_LEFT:
                 left = True
            elif event.key == pygame.K_RIGHT:
                 right = True
            elif event.key == pygame.K_LEFT:
                 left = True


         elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                 right = False
            elif event.key == pygame.K_LEFT:
                 left = False
            if event.key == pygame.K_LSHIFT:
               walk = True

      # only do something if the event is of type QUIT
         if event.type == pygame.QUIT:
         # change the value to False, to exit the main loop
            running = False
            sys.exit()


      # moving left
      if left == True and rightcounter == 0:
         leftcounter = leftcounter + 1
         if walk == True:
            leftcounter = leftcounter - 5
            if leftcounter < 1:
               leftcounter = 1
         if leftcounter >= 1:
            char.vx = -1
         if leftcounter >= 8  and walk == False:
            char.vx = -2
         if leftcounter >= 15  and walk == False:
            char.vx = -3
            leftcounter = 15
      
      #stopping left   
      if left == False and rightcounter == 0:
         leftcounter = leftcounter - 5
         if leftcounter <= 0:
            char.vx = 0
            leftcounter = 0
         if leftcounter >= 1:
            char.vx = -1
         if leftcounter >= 8:
            char.vx = -2
      
      # moving right
      if right == True and leftcounter == 0:
         rightcounter = rightcounter + 1
         if walk == True:
           rightcounter = rightcounter - 5
           if rightcounter < 1:
             rightcounter = 1
         if rightcounter >= 1:
            char.vx = 1
         if rightcounter >= 8 and walk == False:
            char.vx = 2
         if rightcounter >= 15 and walk == False:
            char.vx = 3
            rightcounter = 15

      # stopping right   
      if right == False and leftcounter == 0:
         rightcounter = rightcounter - 5
         if rightcounter <= 0:
            char.vx = 0
            rightcounter = 0   
         if rightcounter >= 1:
            char.vx = 1
         if rightcounter >= 8:
            char.vx = 2      
      
      beta = level[char.y + 10, char.x: char.x + 5]
      omega = level[char.y - 1, char.x:char.x + 5]

      if jumping == False:
         jumpcounter = 0
         if all(beta == 0) == True:
            falling = True
            jump = False
            fallcounter = fallcounter + 1
            if fallcounter <= 0:
               char.vy = 0
               fallcounter = 0   
            if fallcounter >= 1:
               char.vy = -1
            if fallcounter >= 3:
               char.vy = -2
            if fallcounter >= 8:
               char.vy = -3
            if fallcounter >= 12:
               char.vy = -4
            char.vx, char.x, char.vy, char.y, level, falling, jump, beta, omega = charcheck.fallcheck(char.vx, char.x, char.vy, char.y, level, falling, jump, beta, omega, totalY)
            if falling == False:
               fallcounter = 0
         if all(beta == 0) == False:
            falling == False
            jump = True
            fallcounter = 0
            char.vy = 0


      if jumping == True and falling == False:

          char.vy = 0
          if all(omega == 0) == True and doublejumpcounter == 1:
            falling = False
            jump = False
            jumpcounter = jumpcounter + 1
            fallcounter = 0
            
            if jumpcounter <= 0:
                 char.vy = 0
                 jumpcounter = 0
            if jumpcounter >= 1:
               char.vy = 3
            if jumpcounter >= 3:
               char.vy = 2
            if jumpcounter >= 7:
                char.vy = 1
            if jumpcounter >= 11:
                jumping = False
                jumpcounter = 0
                char.vy = 0
            char.vx, char.x, char.vy, char.y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega = charcheck.jumpcheck(char.vx, char.x, char.vy, char.y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega)

          if all(omega == 0) == True and doublejumpcounter == 2:
            falling = False
            jump = False
            jumpcounter = jumpcounter + 1
            fallcounter = 0
            if jumpcounter <= 0:
                 char.vy = 0
                 jumpcounter = 0
            if jumpcounter >= 1:
               char.vy = 2
            if jumpcounter >= 5:
               char.vy = 1
            if jumpcounter >= 10:
                jumping = False
                jumpcounter = 0
                char.vy = 0
            char.vx, char.x, char.vy, char.y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega = charcheck.jumpcheck(char.vx, char.x, char.vy, char.y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega)
          elif all(omega == 0) == False:
             char.vy = 0
             jumpcounter = 0
             jumping = False

      beta = level[char.y + 10, char.x: char.x + 5]
      omega = level[char.y - 1, char.x:char.x + 5]
      if all(omega == 0) == False and all(beta == 0) == False:
         jump = False
         falling = False
         jumping = False
         doublejumpcounter = 0
         fallcounter = 0

      if all(omega == 0) == True and all(beta == 0) == False:
         jump = True
         falling = False
         jumping = False
         doublejumpcounter = 0

      if all(omega == 0) == False and all(beta == 0) == True:
         jump = True
         falling = True
         jumping = False

      if all(omega == 0) == True and all(beta == 0) == True and jumping == False:
         jump = True
         falling = True
         jumping = False

      if all(omega == 0) == True and all(beta == 0) == True and jumping == True:
         jump = False
         falling = False
         jumping = True

      char.vx, char.x, char.vy, char.y, level = charcheck.movecheck(char.vx, char.x, char.vy, char.y, level, totalX)


