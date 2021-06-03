import random
def setup():
    size(450,600) 


sizeWidth = 5
sizeHeight = 5


ran = random.randint(0,3)

tiles = [0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0]

tCheck = [0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0,
          0,0,0,0,0]

counter = -1


for i in range(25):
    counter += 1
    ran = random.randint(0,2)
    if ran == 2:
        tCheck[counter] = 1

    elif ran <= 2:
        tCheck[counter] = 0

print(tCheck)

#counter = -1
#for j in range(sizeHeight):
#    for i in range(sizeWidth):
#        counter += 1
#        tiles.append(0)
        

#1 comes first, it's all the way to the left or all the way on top

topN1 = [] 

topN2 = [0,0,0,0,0]

topN3 = [0,0,0,0,0]

sideN1 = [0,0,0,0,0]

sideN2 = [0,0,0,0,0]

sideN3 = [0,0,0,0,0]

counter = 0

thing = [0]

counter = -1


tc1 = -1
t1 = 0
ct11 = [0]

#top 1

for i in range(5):
    counter += 1
    tc1 += 1
    if tCheck[counter*5] == 1:
        t1 += 1
    elif tCheck[counter*5] == 0 and t1 > 0:
        ct11[0] = 1
    elif tCheck[counter*5] == 0 and t1 == 0:
        t1 += 0

#top 2
tc2 = -1
counter = -1
t2 = 0
ct2 = [0]

for i in range(5):
    counter += 1
    tc2 += 1
    if tCheck[counter*5+1] == 1:
        t2 += 1
    elif tCheck[counter*5+1] == 0 and t2 > 0:
        ct2[0] = 1
    elif tCheck[counter*5+1] == 0 and t2 == 0:
        t2 += 0
        
        
#top 3
tc1 = -1
counter = -1
t3 = 0
ct3 = [0]

for i in range(5):
    counter += 1
    tc1 += 1
    if tCheck[counter*5+2] == 1:
        t3 += 1
    elif tCheck[counter*5+2] == 0 and t3 > 0:
        ct3[0] = 1
    elif tCheck[counter*5+2] == 0 and t3 == 0:
        t3 += 0
        
        
#top 4
tc4 = -1
counter = -1
t4 = 0
ct4 = [0]

for i in range(5):
    tc4 += 1
    counter += 1
    if tCheck[counter*5+3] == 1:
        t4 += 1
    elif tCheck[counter*5+3] == 0 and t4 > 0:
        ct4[0] = 1
    elif tCheck[counter*5+3] == 0 and t4 == 0:
        t4 += 0


#top 5
tc5 = -1
counter = -1
t5 = 0
ct5 = [0]

for i in range(5):
    tc5 += 1
    counter += 1
    if tCheck[counter*5+4] == 1:
        t5 += 1
    elif tCheck[counter*5+4] == 0 and t5 > 0:
        ct5[0] = 1
    elif tCheck[counter*5+4] == 0 and t5 == 0:
        t5 += 0
        
        
#top 1 2 
ct12 = [0]
tc1 -= 1
t12 = 0
if ct11[0] == 1:
    tc1 += 1
    if tCheck[tc1*5] == 1:
        t12 += 1
    elif tCheck[tc1*5] == 0 and t12 > 0:
        ct12[0] = 1
    elif tCheck[tc1*5] == 0 and t12 == 0:
        t12 += 0
        
        



#top 2 2 
ct22 = [0]
tc2 -= 1
t22 = 0
if ct2[0] == 1:
    tc1 += 1
    if tCheck[tc1*5] == 1:
        t12 += 1
    elif tCheck[tc1*5] == 0 and t12 > 0:
        ct12[0] = 1
    elif tCheck[tc1*5] == 0 and t12 == 0:
        t12 += 0
        
#top 3 2 
ct12 = [0]
tc1 -= 1
t12 = 0
if ct11[0] == 1:
    tc1 += 1
    if tCheck[tc1*5] == 1:
        t12 += 1
    elif tCheck[tc1*5] == 0 and t12 > 0:
        ct12[0] = 1
    elif tCheck[tc1*5] == 0 and t12 == 0:
        t12 += 0
        
#top 4 2 
ct12 = [0]
tc1 -= 1
t12 = 0
if ct11[0] == 1:
    tc1 += 1
    if tCheck[tc1*5] == 1:
        t12 += 1
    elif tCheck[tc1*5] == 0 and t12 > 0:
        ct12[0] = 1
    elif tCheck[tc1*5] == 0 and t12 == 0:
        t12 += 0
        
#top 5 2 
ct12 = [0]
tc1 -= 1
t12 = 0
if ct11[0] == 1:
    tc1 += 1
    if tCheck[tc1*5] == 1:
        t12 += 1
    elif tCheck[tc1*5] == 0 and t12 > 0:
        ct12[0] = 1
    elif tCheck[tc1*5] == 0 and t12 == 0:
        t12 += 0
        
        

def draw():
    global tileX, tileY, thing, topN1
    background(0,0,0)
    textSize(35)
    fill(0,0,0)
    stroke(255,255,255)
    for j in range(int(sizeHeight)):
        for i in range(int(sizeWidth)):
            rect(i * 50 + 150, j * 50 + 150, 50,50) 
    
    for i in range(sizeWidth):
        rect(i * 50 + 150, 50, 50, 100)
    
    for i in range(sizeHeight):
        rect(50, i*50+150,100, 50)
    
    rect(150, 450, 250, 100)
    
    fill(255,255,255)
    
    text("Done", 230, 510)
    
    tileX = mouseX/50 -2
    tileY = mouseY/50 -2
    
    fill(255,255,255)
    
    counter = 0
    
    counter = -1
    
    
    textSize(25)
    
    
    if ct11[0] == 1:
        text(str(t1), 168, 87)
    
    if ct2[0] == 1:
        text(str(t2), 218, 87)
    
    if ct3[0] == 1:
        text(str(t3), 267, 87)
        
    if ct4[0] == 1:
        text(str(t4), 317, 87)
        
    if ct5[0] == 1:
        text(str(t5), 368, 87)
        
    
    
    if ct11[0] == 1:
        text(str(t12), 168, 107)
        
        
    counter = 0
    
    if thing[counter] == 1:
        textSize(10)
        fill(0,255,0)
        text("Congrats!", 150, 30)

        
    elif thing[counter] == 2:
        textSize(10)
        fill(255,0,0)
        text("ur bad!", 150, 30)
        
    counter = -1
        
    
    for j in range(int(sizeHeight)):
        for i in range(int(sizeWidth)):
            counter += 1
            if tiles[counter] == 1:
                rect(i * 50 + 155, j * 50 + 155, 40,40) 
                
    
    #for j in range(int(sizeHeight)):
        #for i in range(int(sizeWidth)):
            #if tileX == (i + 1) and tileY == (j + 1):
                #rect(i * 50 + 155, j * 50 + 155, 40,40) 
    textSize(25)

    
    
        

def mouseClicked():
    tileX = mouseX/50 -2
    tileY = mouseY/50 -2
    counter = -1
    for j in range(int(sizeHeight)):
        for i in range(int(sizeWidth)):
            counter += 1
            if tileX == (i + 1) and tileY == (j + 1):
                if tiles[counter] == 1:
                    tiles[counter] = 0
                elif tiles[counter] == 0:
                    tiles[counter] = 1
    counter = 0
                    
    if mouseX >= 150 and mouseX <= 400 and mouseY >= 450 and mouseY <= 550:
        if tiles == tCheck:
            textSize(10)
            fill(0,255,0)
            text("Congrats!", 150, 30)
            thing[counter] = 1
        else:
            textSize(10)
            fill(255,0,0)
            text("ur bad!", 150, 30)
            thing[counter] = 2
