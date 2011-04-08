'''
Created on 8 avr. 2011

@author: JD219546
'''

class CheckingStockManager(object):
    '''
    classdocs
    '''


    def __init__(self, stockManager):
        '''
        Constructor
        '''
        self.stockManager = stockManager
    
    def check_not_negative_stock(self,stock):
        i = 0
        for res in stock.stock_dict.keys():
            if stock.stock_dict[res][0] < 0:
                print (i,"stock Negative for resource",res.name,":",stock.stock_dict[res][0])
                stock.print_stock()
                return False
            i += 1
        return True    
        
    def test_not_negative_stocks(self):
        all_stocks =  self.stockManager.get_all_stocks()
        for st in all_stocks:
            if not self.check_not_negative_stock(st):
                return False
        return True
    
    def check_not_superior_max_stock(self,stock):
        for res in stock.stock_dict.keys():
            if stock.stock_dict[res][0] > stock.stock_dict[res][1]:
                return False
        return True        
    
    def test_not_superior_max_stocks(self):
        all_stocks =  self.stockManager.get_all_stocks()
        for st in all_stocks:
            if not self.check_not_superior_max_stock(st):
                return False
        return True
    
    def test(self):
        if self.test_not_negative_stocks():
            if self.test_not_superior_max_stocks():
                return True
            else:
                raise Exception("Stock superior to maximum")
        else:
            raise Exception("Stock negative")