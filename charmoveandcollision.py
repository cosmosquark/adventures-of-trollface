def charlocation(x, y, totalX, totalY, halfresX, halfresY):
   if x < halfresX:
      placeX = halfresX
   if x >= halfresX and x <= totalX - halfresX:
      placeX = x
   if x >= totalX - halfresX:
      placeX = totalX - halfresX
   if y < halfresY:
      placeY = halfresY
   if y >= halfresY and y <= totalY - halfresY:
      placeY = totalY - y
   if y >= totalY - halfresY:
      placeY = totalY - halfresY
   return placeX, placeY

def movecheck(vx, x, vy, y, level, totalX):
     if vx >= 1 and x < totalX-7:
        for i in range(0, vx):
           alpha = level[y:y + 10,x + 6]
           if all(alpha == 0) == True and x < totalX - 7:
              x = x + 1
              level[y:y + 10,x:x + 5] = 2
              level[y:y + 10,x - 1] = 0
           else:
              break

     elif vx <= -1 and x > 0:
        for i in range(0, abs(vx)):
           alpha = level[y:y + 10,x - 1]
           if all(alpha == 0) == True and x > 0:
             x = x - 1
             level[y:y + 10,x:x + 5] = 2
             level[y:y + 10,x + 5] = 0
           else:
             break
     
     return vx, x, vy, y, level

def fallcheck(vx, x, vy, y, level, falling, jump, beta, omega, totalY):
   beta = level[y + 10, x: x + 5]
   if all(beta == 0) == False:
      Falling = False
      jump = True
      return vx, x, vy, y, level, falling, jump, beta, omega
   
   if y >= totalY - 11:
      level[y:y + 10, x: x + 5] = 0
      placeX = 40
      y = 10
      x = 10
      level[y:y + 10, x: x + 5] = 2
      beta = level[y + 10, x: x + 5]
      return vx, x, vy, y, level, falling, jump, beta, omega

   beta = level[y + 10, x: x + 5]
   if falling == True and y < 50:
      if vy <= -1:
         for i in range(0, abs(vy)):
            beta = level[y + 10, x: x + 5]
            if all(beta == 0) == True:
              y = y + 1
              level[y:y + 10,x:x + 5] = 2
              level[y-1,x:x + 5] = 0
              falling = True
              jumping = False
            elif all(beta == 0) == False:
              falling = False
              jumping = False
              vy = 0
              jump == True
              return vx, x, vy, y, level, falling, jump, beta, omega
              break
            if y >= 49:
              print "You mad?"
              level[y:y + 10, x: x + 5] = 0
              placeX = 40
              y = 10
              x = 10
              level[y:y + 10, x: x + 5] = 2
              beta = level[y + 10, x: x + 5]
              return vx, x, vy, y, level, falling, jump, beta, omega
              break
            beta = level[y + 10, x: x + 5]
              

   return vx, x, vy, y, level, falling, jump, beta, omega

def jumpcheck(vx, x, vy, y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega):
   omega = level[y - 1, x: x + 5]
   if y <= 2:
      falling = True
      jumping = False
      jumpcounter = 0

   if all(omega == 0) == False:
      jumping = False
      falling = True
      jumpcounter = 0
      return vx, x, vy, y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega
      
   elif jumping == True and y > 1 and doublejumpcounter < 3:
      if vy >= 1:
         for i in range(0, abs(vy)):
            omega = level[y - 1, x: x + 5]
            if all(omega == 0) == True:
              y = y - 1
              level[y:y + 10,x:x + 5] = 2
              level[y+10,x:x + 5] = 0
              falling = False
              jumping = True
            elif all(omega == 0) == False:
              falling = True
              jumping = False
              vy = 0
              jump == False
              jumpcounter = 0
              break
              
            omega = level[y + 10, x: x + 5]

   return vx, x, vy, y, level, falling, jump, jumping, jumpcounter, doublejumpcounter, beta, omega
