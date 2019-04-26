import json 
import requests
import panda as pd

r = requests.get('http://localhost:3000/')

data =r.json()

#pop = input("Enter state")

#if(pop=="Alabama"):
   # print(data[0]['States '] + " " +"is" + " "+ data[0]['Population Estimates'])
#print(data)





#print(data[1]['name'] + " " +"is" + " "+ data[1]['color'])
#print(data[2]['name'] + " " +"is" + " "+ data[2]['color'])
#print(data[3]['name'] + " " +"is" + " "+ data[3]['color'])



if(pop=="Alabama"):
    print(d[0]['States '] + " " +"is" + " "+ d[0]['Population Estimates'])
    pygame.init()

    display_width = 400
    display_height = 400

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    black=(0,0,0)
    white = (255,255,255)

    crashed = False
    carImg = pygame.image.load('c:/cap.jpg')

    #s=d[0]['States '] + " " +"is" + " "+ d[0]['Population Estimates']

    #print(s)
    

    # def tex(a,b):
    #     gameDisplay.blit(display,(a,b))
    
    # a=(display_width*0.21)
    # b=(display_height*0.5)

    # myFont=pygame.font.Font("Times New Roman",118)

    # display1 =myFont.render(str(s),1,white)
    
    # pygame.display1.update()

    def car(x,y):
        gameDisplay.blit(carImg, (x,y))

    x =  (display_width )
    y = (display_height )


    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        car(x,y)
        #tex(a,b)
        
        
        pygame.display.update()
        

    pygame.quit()
    quit()