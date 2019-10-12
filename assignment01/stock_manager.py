"""
Implement here your solution
NOTE that the package assignment01 must contain 
"""

from stack import ArrayStack

class StockManager:
    def __init__(self):
        self.companies = ('Apple', 'Google', 'BMW')
        self.apple = ArrayStack()
        self.google = ArrayStack()
        self.bmw = ArrayStack()
        self._total_profit = 0 # intended as non-public, should be accessed with self.get_profit()
    
    def __getitem__(self, key):
        """ 
        This method allow you to use brackets [ ] with self. ex: self[company]
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
        return self._total_profit
    
    def buy_shares(self, company, number, buy_price):
        """
        Method to buy shares of one company

        comapany : string, "Apple", "Google" or "BMW"\n
        number : int, number of shares you want to buy\n
        buy_price : int or float, the price you want to buy shares at

        """        
        if company not in self.companies:
            raise ValueError(f'"{company}" is not managed in the app.')    
        
        if not isinstance(number, int):
            raise TypeError('Number of shares must be an integer')
        if number <= 0:
            raise ValueError(f'Cannot buy {number} shares')
        
        
        if not isinstance(buy_price, (int, float)):
            raise TypeError('Buy price must be numeric')
        elif buy_price <= 0:
            raise ValueError(f'Buy price cannot be negative')

        self[company].push([number, buy_price])


    def buy_multiple(self, company_list, number_list, buy_price_list):
        
        if len(company_list) != len(number_list) != len(buy_price_list):
            print('Error: Lengths of lists are not equal')
            return

        orders = len(company_list)
        for i in range(0, orders):
            order = [company_list[i], number_list[i], buy_price_list[i]]
            try:
                self.buy_shares(order[0], order[1], order[2])
            except ValueError:
                raise
            except TypeError:
                raise

    def sell_share(self, company, number, sell_price):
        if company not in self.companies:
            raise ValueError(f'"{company}" is not managed in the app.')    
        
        if not isinstance(number, int):
            raise TypeError('Number of shares must be an integer')
        if number <= 0:
            raise ValueError(f'Cannot sell {number} shares')
        
        
        if not isinstance(sell_price, (int, float)):
            raise TypeError('Sell price must be numeric')
        elif sell_price <= 0:
            raise ValueError(f'Sell price cannot be negative')
        
        print('printing',self[company])
        print('printing',self.apple)

        # if company == 'Apple':
        #     if self.apple.is_empty():
        #         print('You do not have Apple stock.')
        #         return
        #     pop = self.apple.pop()
        #     if pop[0] >= number:
        #         shares_left = pop[0] - number
        #         profit = ((number*sell_price) - (number*pop[1]))
        #         self.total_profit += profit
        #         if shares_left != 0:
        #             self.apple.push([shares_left, pop[1]])
        #         return 
        #     elif pop[0] < number:
        #         number -= pop[0]
        #         profit = ((pop[0]*sell_price) - (pop[0]*pop[1]))
        #         self.total_profit += profit
        #         return self.sell_share('Apple', number, sell_price)
            
        # elif company == 'Google':
        #     self.google.push([number, buy_price])
        #     pass
        # elif company == 'BMW':
        #     self.bmw.push([number, buy_price])
        
   

    # def sell_multiple(self, company_list, number_list, sell_price_list):

manager = StockManager()
manager.buy_shares("Apple", 10, 5)
manager.buy_shares("Google", 120, 5)
manager.buy_shares("BMW", 110, 5)
manager.apple.print_contents()
manager.google.print_contents()
manager.bmw.print_contents()
# manager.sell_share('Apple', 100, 10)
# manager.apple.print_contents()
print(manager.get_profit())
