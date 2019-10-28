"""
NOTE that the package assignment01 contains linkedStack.py
"""

from linkedStack import LinkedStack


class Company:
    def __init__(self, name):
        self.name = name
        self.shares_owned = LinkedStack() 
        self.sell_all = False     

    def get_total_shares(self):
        total = 0
        if not self.shares_owned.is_empty():
            top = self.shares_owned.top()
            while top:
                total += top.data[0]
                top = top.next
        return total


    
class StockManager:
    def __init__(self):
        self.companies = ('Apple', 'Google', 'BMW')
        self.apple = Company('Apple') # uses company class
        self.google = Company('Google')
        self.bmw = Company('BMW')
        self._net = 0

    
    def __getitem__(self, key):
        """ 
        This method allows us to use brackets [ ] with self. ex: self[company]
        """
        if key == 'Apple':
            return self.apple
        elif key == 'Google':
            return self.google
        elif key == 'BMW':
            return self.bmw
        return False


    def get_profit(self):
        """
        Returns the net income/loss resulting from your buy & sell operations
        """

        # if self._net > 0:
        #     print(f'You made {self._net} (profit) from your transactions')
        # elif self._net < 0:
        #     print(f'You made {self._net} (loss) from your transactions')
        # else:
        #     print(f'You did not make profit/loss. Your net is 0')

        # the block above can be uncommented if we need to print the net value. But we don't need it now.
        
        return self._net
    
    def buy_shares(self, company, number, buy_price):
        """
        Method to buy shares of one company

        comapany : string, "Apple", "Google" or "BMW"\n
        number : int, number of shares you want to buy\n
        buy_price : int or float, the price you want to buy shares at

        """  

        if company not in self.companies:
            raise ValueError(f'"{company}" is not managed in this program.')    
        
        if not isinstance(number, int):
            raise TypeError('Number of shares must be an integer')
        if number <= 0:
            raise ValueError(f'Cannot buy {number} shares')
        
        
        if not isinstance(buy_price, (int, float)):
            raise TypeError('Buy price must be numeric')
        elif buy_price <= 0:
            raise ValueError(f'Buy price cannot be negative')

        self[company].shares_owned.push([number, buy_price]) 
        

    def buy_multiple(self, company_list, number_list, buy_price_list):
        """
        Method to buy shares of multiple companies

        comapany_list : list of companies (string), "Apple", "Google" or "BMW"\n
        number_list : list of numbers (integer) of shares you want to buy\n
        buy_price_list : list of prices (int, float) you want to buy shares at

        """        

        samelength = (len(company_list) == len(number_list) == len(buy_price_list))
        
        if not samelength:
            print('Error: Lengths of lists are not equal')
            return False

        for i in range(0, len(company_list)):
        
             try:
                self.buy_shares(company_list[i], number_list[i], buy_price_list[i])
             except (ValueError, TypeError):
                 raise 

    def sell_shares(self, company, number, sell_price, profit = 0):
        """
        Method to sell shares of one company

        comapany : string, "Apple", "Google" or "BMW"\n
        number : int, number of shares you want to sell\n
        sell_price : int or float, the price you want to sell shares at\n
        profit : default value 0 (initially, if not provided in a recursive function later)

        """        

        if company not in self.companies:
            raise ValueError(f'"{company}" is not managed in this program.')    
        
        if not isinstance(number, int):
            raise TypeError('Number of shares must be an integer')
        if number <= 0:
            raise ValueError(f'Cannot sell {number} shares')
        
        
        if not isinstance(sell_price, (int, float)):
            raise TypeError('Sell price must be numeric')
        elif sell_price <= 0:
            raise ValueError(f'Sell price must be a positive number')
        
        if self[company].shares_owned.is_empty():
            self._net += profit
            return profit
        
        shares_owned = self[company].get_total_shares()
        
        if not self[company].sell_all and shares_owned < number:
            answer = input(f'\nYou own only {shares_owned} shares of "{company}", which is less than what you want to sell ({number}).\nWould you like to sell your {shares_owned} shares?\n' )
            if answer.strip() == 'YES':
                self[company].sell_all = True
                pass
            else:
                return False


        pop = self[company].shares_owned.pop()
        # pop is a list containing number & price pair --> [number, price]. Thus:
        # pop[0] is number of shares
        # pop[1] is the price at which shares have been bought  

        if pop[0] < number:
            number -= pop[0]
            profit += (pop[0]*(sell_price - pop[1]))
            return self.sell_shares(company, number, sell_price, profit)            
        elif pop[0] >= number:
            shares_left = pop[0] - number
            profit += (number*(sell_price - pop[1]))
            if shares_left > 0:                
                self[company].shares_owned.push([shares_left, pop[1]])
            self._net += profit
            return profit
        

    def sell_multiple(self, company_list, number_list, sell_price_list):
        """
        Method to sell shares of multiple companies

        comapany_list : list of companies (string), "Apple", "Google" or "BMW"\n
        number_list : list of numbers (integer) of shares you want to sell\n
        buy_price_list : list of prices (int, float) you want to sell shares at

        """   

        samelength = (len(company_list) == len(number_list) == len(sell_price_list))
        
        if not samelength:
            print('Error: Lengths of lists are not equal')
            return False
 
        for i in range(0, len(company_list)):
            try:
                self.sell_shares(company_list[i], number_list[i], sell_price_list[i])
            except (ValueError, TypeError):
                raise
        


""" main() to do some testing"""
if __name__ == '__main__':

    manager = StockManager()

    # test buy methods
    print('\nTesting buy methods...\n')
    manager.buy_shares("Apple", 1000, 120)
    manager.buy_shares("Google", 1000, 115)
    manager.buy_multiple(['Apple', 'BMW'], [1000, 5000], [125, 80])
    # manager.buy_shares('Tesla', 100, 100)


    print('Total shares of "Apple": ', manager.apple.get_total_shares()) # must print 2000
    print('Total shares of "Google": ', manager.google.get_total_shares()) # must print 1000
    print('Total shares of "BMW": ', manager.bmw.get_total_shares()) # must print 5000

    print('Profit / loss: ', manager.get_profit()) # must print 0, because we did not do any sale, only bought


    # test sell methods
    print('\nTesting sell methods...\n')
    manager.sell_shares('Apple', 500, 110)
    manager.sell_shares("Google", 500, 110) 
    manager.sell_multiple(['Apple', 'BMW'], [1000, 4000], [125, 85]) 
    # manager.sell_shares('Google', 600, 150)   


    print('Total shares of "Apple": ', manager.apple.get_total_shares()) 
    print('Total shares of "Google": ', manager.google.get_total_shares())
    print('Total shares of "BMW": ', manager.bmw.get_total_shares())
  
    print('\nProfit / loss: ', manager.get_profit(), '\n')

