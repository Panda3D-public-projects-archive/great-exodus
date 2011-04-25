'''
Created on 8 avr. 2011

@author: JD219546
'''
import threading
import time

class ProductionTimer(threading.Thread):
    def __init__(self, tempo, resource):
        self.func = self.evolve_stock
        self.tempo = tempo
        self.resource = resource
        self.production_object_list = []
        self.running = False
        threading.Thread.__init__(self,name = "PeriodicExecutor")
        self.keep_on_waiting_for_work = True
        self.setDaemon(1)
        #self._timer = threading.Timer(self._tempo, self._run)

    def run(self):
        self.running = True
        while self.keep_on_waiting_for_work:
            time.sleep(0.1)
            while (self.running):
                self.evolve_stock()

    def pause(self):
        self.running = not self.running
        #self._timer.cancel()      
        
    def terminate(self):
        self.keep_on_waiting_for_work = False    
        
    def add_production_object(self, production_object):
        self.production_object_list.append(production_object)  
            
    def evolve_stock(self):
        production = 0
        for po in self.production_object_list:
            if po.can_produce(self.resource):
                po.evolve_stock(self.resource)
                production += 1
        if production == 0:
            self.pause() 
            
    def is_running(self):
        return self.running#self._timer.isAlive() 

class ProductionTimerFactory(object):
    '''
    classdocs
    '''

    def get_production_timer(self, resource):
        return self.time_interval_dict[resource]

    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        #defining intervals
        self.time_interval_dict = {}
        self.time_interval_dict[resource_manager.food] = 3
        self.time_interval_dict[resource_manager.crystal] = 3
        self.time_interval_dict[resource_manager.gaz] = 3        
        self.time_interval_dict[resource_manager.chip] = 3
        self.time_interval_dict[resource_manager.fuel] = 2
        self.time_interval_dict[resource_manager.ice] = 1
        self.time_interval_dict[resource_manager.ore] = 1
        self.time_interval_dict[resource_manager.steel] = 8
        self.time_interval_dict[resource_manager.radar] = 3
        self.time_interval_dict[resource_manager.shield_generator] = 3
        self.time_interval_dict[resource_manager.engine] = 3
        self.time_interval_dict[resource_manager.hull] = 2
        self.time_interval_dict[resource_manager.life_support] = 2
        
        #defining timers
        self.timer_map = {}
        for res in resource_manager.resource_list:
            self.create_timer_and_add_to_map(res)

    def create_timer_and_add_to_map(self, resource):
        pt = ProductionTimer(self.time_interval_dict[resource], resource)
        self.add_timer_to_map(pt)
        return pt
        
    def add_timer_to_map(self, timer):
        self.timer_map[timer.resource] = timer
        
    def add_small_production_object(self, prodObj):
        for prod_res in prodObj.getProduced_resources():
            self.timer_map[prod_res].add_production_object(prodObj)    
    
    def start_global_production(self):
        for ti in self.timer_map.values():
            ti.start()
            
    def is_global_production_stalled(self):
        still_running = False
        for ti in self.timer_map.values():
            still_running = still_running or ti.is_running()
        return still_running == False
    
    def terminate_timers(self):
        for ti in self.timer_map.values():
            ti.terminate()
        