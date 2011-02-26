from math import* 

class Noeud:

    def __init__(self, coutG, coutH, coutF, paren):
        self.cout_g = coutG
        self.cout_h = coutH
        self.cout_f = coutF
        self.parent = paren

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __hash__(self):
        return 1
    
    @staticmethod
    def distance(p1, p2):
        return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

class Config:
    
    def __init__(self, xmin, xmax, ymin, ymax, tab, pointDe, pointAr):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.tab = tab
        self.pointDe = pointDe
        self.pointAr = pointAr
    
    def estAcc(self,pt1):
        a = (pt1.x >= self.xmin and pt1.x < self.xmax)
        a = (a and pt1.y >= self.ymin and pt1.y < self.ymax)
        a = (a and not (pt1 in self.tab))
        return (not a) 
        
