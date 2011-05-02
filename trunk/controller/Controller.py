'''
Created on 18 avr. 2011

@author: JD219546
'''
import time
from core.ResourcesPackage.ResourcesManager import ResourcesManager
from core.ResourcesPackage.StockManager import StockManager
from core.ProductionPackage.ProductionManager import ProductionManager
from trunk.core.trade.TraderManager import TraderManager
from controller.ControllerTimer import ControllerTimer




class Controller(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

        self.resource_manager = ResourcesManager()
        self.stock_manager = StockManager(self.resource_manager,1) 
        self.production_manager = ProductionManager(self.resource_manager)
        self.trader_manager = TraderManager()
        self.controller_timer = ControllerTimer()
        self.nb_iterations = 0
        
        

        
    def run(self, iterations = 25):
        self.controller_timer.start()
        for i in range(iterations):
            #print("Iteration",i,"@",self.previous_start_time)
            self.production_manager.update(i)
            self.controller_timer.wait()
            self.nb_iterations += 1
            
