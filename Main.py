#----------------------------- actual code --------------------------------

# import the pygame module, so you can use it
import pygame
import pygame.gfxdraw
import random
from Noeud import *


def CalculA(listF,listO,listPt):
    i = 1
    while i<250:
        x = random.randint(0, 40)
        y = random.randint(0, 40)
        if(x != 250 and y != 320):      
            listPt.append(Point(x*10,y*10))
        i += 1
    configDef = Config(0, 400, 0, 400, listPt, Point(0,0), Point(350,120))
    a = Point.distance(configDef.pointDe,configDef.pointAr)
    b = Noeud(0,a,a,None)
    listF[configDef.pointDe] = b
    return configDef
    
def presentList(list,pt):
    return pt in list.keys()
        
def ajoutcase(listF,listO,point1,config):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if(i==0 and j==0):
                continue
            x = point1.x + i*10
            y = point1.y + j*10
            if (config.estAcc(Point(x,y))):
                continue
            if (not presentList(listF,Point(x,y))):
                key = listF.get(point1)
                coutG = key.cout_g + Point.distance(point1,Point(x,y))
                coutH = Point.distance(Point(x,y),config.pointAr)
                coutF = coutH + coutG
                if (presentList(listO, Point(x,y))):
                    keyO = listO.get(Point(x,y))
                    if(coutF < keyO.cout_f ):
                        key0 = Noeud(coutG, coutH, coutF, point1)
                else:
                    listO[Point(x,y)]=Noeud(coutG, coutH, coutF, point1)

def desChem(listF,screen,colorR):
    iterA = listF.keys()                     
    for pt1 in iterA:
        rec = pygame.Rect(pt1.x, pt1.y, 10, 10)
        pygame.draw.rect(screen, colorR, rec)
    pygame.display.flip()
    
def desChemFin(listPt,screen,colorR):              
    for pt1 in listPt:
        rec = pygame.Rect(pt1.x, pt1.y, 10, 10)
        pygame.draw.rect(screen, colorR, rec)
    pygame.display.flip()
    
def calMin(listO,listF,ptEnd):
    iterA = listO.keys() 
    pt = None
    noeudTemp = Noeud(100000, 100000, 100000, None)                 
    for pt1 in iterA:
        noeud1 = listO[pt1]
        if (noeud1.cout_f < noeudTemp.cout_f):
            pt = pt1
            noeudTemp = noeud1
    listF[pt] = noeudTemp
    del listO[pt]
    if (pt == ptEnd):
        return Point(-1,-1)
    return pt

def calChem(listPt,listF,ptEnd):
    listPt.append(ptEnd)
    noeudT = listF[ptEnd]
    par = noeudT.parent
    while not (par is None):
        noeudT = listF[par]
        listPt.append(par)
        par = noeudT.parent

def main():
        
    # initialize the pygame module
    pygame.init()
    
    pygame.display.set_caption("minimal program")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((400,400))
    pygame.display.get_surface().fill((255,255,255))
    

    listF = dict()
    listO = dict()
    listPt = []
    configDef = CalculA(listF,listO,listPt)

    
    ajoutcase(listF,listO,configDef.pointDe,configDef)
    desChem(listF,screen,(255,0,0))   
    desChem(listO,screen,(0,255,0))
    
    i=0
    while i<1000:
        pt2 = calMin(listO,listF,configDef.pointAr)
        if (pt2 == Point(-1,-1)):
            break
        ajoutcase(listF,listO,pt2,configDef)
        desChem(listF,screen,(255,0,0))   
        desChem(listO,screen,(0,255,0))
    
        i+=1
    
    listPt2=[]
    
    calChem(listPt2,listF,configDef.pointAr)
    
    desChemFin(listPt,screen,(0,0,0))
    desChemFin(listPt2,screen,(0,255,255))
    
    rec = pygame.Rect(configDef.pointAr.x, configDef.pointAr.y, 10, 10)
    pygame.draw.rect(screen, (50,50,50), rec)
    pygame.display.flip()
    
    running = True   
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    
