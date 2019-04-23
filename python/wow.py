import pygame
import json
with open("C:\data.json") as json_data:
    d=json.load(json_data)
    

nameofState= input("Enter state ")   #Get user input

if(nameofState=="Alabama"):  
    print(d[0]['States '] +"'s" +" " +"population Estimate is" + " "+ d[0]['Population Estimates'])  #print state name and population estimates from the 0 index

    pygame.init()  #initiates pygame module 

    display_width = 600
    display_height = 400

    gameDisplay = pygame.display.set_mode((display_width,display_height)) #sets the size of the window
    pygame.display.set_caption('State Image') #Name of window

    white = (255,255,255)  #defines the color of the window

    
    show = True
    stateImg = pygame.image.load('c:/Alabama.jpg')

    def displayImg(x,y):
        gameDisplay.blit(stateImg, (x,y))

    x =  (display_width/3.5)
    y = (display_height/3)

    while show:
        gameDisplay.fill(white)  #fill window with white color
        displayImg(x,y)          #display image at x,y 
        pygame.display.update()  #updates window
        

        for event in pygame.event.get(): #iterate over the list of Event objects 
                                         #that was retured by the pygame,event.get() method   
             if event.type == pygame.QUIT:
                 show = False
                 
    pygame.quit() #deactivate the pygame library
    quit() #quit the program




elif(nameofState=="California"):
    print(d[4]['States '] +"'s" +" " +"population Estimate is" + " "+ d[4]['Population Estimates'])

    pygame.init()

    display_width = 800
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('State Image')

    white = (255,255,255)

    show = True
    stateImg = pygame.image.load('c:/California.jpg')

    def displayImg(x,y):
        gameDisplay.blit(stateImg, (x,y))

    x =  (display_width / 4)
    y = (display_height /4)

    while show:
        gameDisplay.fill(white)  #fill window with white color
        displayImg(x,y)          #display image at x,y 
        pygame.display.update()  #updates window
        

        for event in pygame.event.get(): #iterate over the list of Event objects 
                                         #that was retured by the pygame,event.get() method   
             if event.type == pygame.QUIT:
                 show = False
                 
    pygame.quit() #deactivate the pygame library
    quit() #quit the program

elif(nameofState=="Ohio"):
    print(d[35]['States '] +"'s" +" " +"population Estimate is" + " "+ d[35]['Population Estimates'])

    pygame.init()

    display_width = 800
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('State Image')

    black = (0,0,0)
    white = (255,255,255)

    
    show = True
    stateImg = pygame.image.load('c:/Ohio.jpg')

    def displayImg(x,y):
        gameDisplay.blit(stateImg, (x,y))

    x =  (display_width/3)
    y = (display_height/4)

    while show:
        gameDisplay.fill(white)  #fill window with white color
        displayImg(x,y)          #display image at x,y 
        pygame.display.update()  #updates window
        

        for event in pygame.event.get(): #iterate over the list of Event objects 
                                         #that was retured by the pygame,event.get() method   
             if event.type == pygame.QUIT:
                 show = False
                 
    pygame.quit() #deactivate the pygame library
    quit() #quit the program

else: 
    print ('Enter a valid state')




