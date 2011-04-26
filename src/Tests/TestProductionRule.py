'''
Created on 24 avr. 2011

@author: JD219546
'''
import unittest
from core.ResourcesPackage.Stock import Stock
from core.ResourcesPackage.ResourcesManager import ResourcesManager
from core.ResourcesPackage.StockLine import StockLine
from core.ProductionPackage.ProductionNeed import ProductionNeed
from core.ProductionPackage.ProductionRule import ProductionRule, ProducedNeededDependencyException
from core.ProductionPackage.ProductionLine import ProductionLine



class TestProductionRule(unittest.TestCase):


    def setUp(self):
        self.resource_manager = ResourcesManager()
        self.engine = "engine"
        self.prod_line_engine = ProductionLine(production_need_list = 
                                         [ProductionNeed("steel"), ProductionNeed("chip")],
                                    production_time_interval = 1, 
                                    quantity_to_produce = 1)
        self.steel = "steel"
        self.prod_line_steel = ProductionLine(production_need_list = 
                                         [ProductionNeed("ore"), ProductionNeed("gaz")],
                                    production_time_interval = 1, 
                                    quantity_to_produce = 1)
        self.ice = "ice"
        self.prod_line_ice = ProductionLine(production_need_list = 
                                         [],
                                    production_time_interval = 1, 
                                    quantity_to_produce = 1)         
        self.food = "food"
        self.prod_line_food = ProductionLine(production_need_list = 
                                         [ProductionNeed("ore"), ProductionNeed(self.ice)],
                                    production_time_interval = 1, 
                                    quantity_to_produce = 1)
   
        self.hull = "hull"
        self.prod_line_hull = ProductionLine(production_need_list = [ProductionNeed(self.steel),],
                                             production_time_interval = 1,
                                             quantity_to_produce = 1)    
        self.production_rule = ProductionRule()
        pass

    def tearDown(self):
        pass


    def test_1_shared_needed_resources_in_same_stock(self):
        p = ProductionRule()
        p.check_and_add_production_line(self.steel, self.prod_line_steel)
        p.check_and_add_production_line(self.food, self.prod_line_food)
        self.assertEqual(len(p.getCareful_needed_resources()),1)
        self.assertTrue("ore" in p.getCareful_needed_resources())
        pass
    
    def test_2_no_shared_needed_resources_in_same_stock(self):
        p = ProductionRule()
        p.check_and_add_production_line(self.steel,self.prod_line_steel)
        p.check_and_add_production_line(self.ice, self.prod_line_ice)
        self.assertFalse(p.getCareful_needed_resources())
        pass
    
    def test_3_shared_needed_and_produced_resources_in_same_stock(self):

        p = self.production_rule
        p.check_and_add_production_line(self.engine, self.prod_line_engine)
        self.assertRaises(ProducedNeededDependencyException, p.check_and_add_production_line, self.steel, self.prod_line_steel)
       
    def test_4_shared_needed_and_produced_resources_in_same_stock_reverse(self):
        p = self.production_rule
        p.check_and_add_production_line(self.steel, self.prod_line_steel)
        self.assertRaises(ProducedNeededDependencyException, p.check_and_add_production_line, self.hull, self.prod_line_hull)       
        pass
    
    def test_5_multiple_production_for_one_rule(self):
        p = self.production_rule
        p.check_and_add_production_line(self.steel, self.prod_line_steel)
        self.assertRaises(ProducedNeededDependencyException, p.check_and_add_production_line, self.hull, self.prod_line_hull)       
        pass

    @staticmethod
    def suite():
        suite = unittest.TestSuite()    
        suite.addTest(unittest.makeSuite(TestProductionRule))
        return suite        
    
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2,buffer=True).run(TestProductionRule.suite())