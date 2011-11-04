'''
Created on 2 mai 2011

@author: benjamin
'''

class Accounts(object):
    '''
    This class represents the accounts of a trader.
    '''


    def __init__(self, credits):
        '''
        Constructor
        '''
        self.credits = credits
        
    def __str__(self):
        return "Accounts: " + str(self.credits) + " credits."

    def get_credits(self):
        return self.credits

    def set_credits(self, credits):
        self.credits = credits

    def increase(self, amount):
        self.set_credits(self.get_credits()+amount)

    def decrease(self, amount):
        self.set_credits(self.get_credits()-amount)
        
        
class TestAccounts(object):
    '''
    This class represents the accounts of a trader.
    '''
        
    def main():
        test_value = 42
        print("Test value is:", test_value)
        accounts = Accounts(test_value)
        print(str(accounts))
        print("Let's set the accounts to 100 credits.")
        accounts.set_credits(100)
        get = accounts.get_credits()
        print("Getter = " + str(get))
        print("Let's add 50 credits to the accounts.")
        accounts.increase(50)
        print(str(accounts))
        print("Let's take off 50 credits from the accounts.")
        accounts.decrease(50)
        print(str(accounts))
        pass
    
    if __name__ == "__main__":
        main()
        pass
        