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
        
        samelength = (len(company_list) == len(number_list) == len(buy_price_list))
        
        if not samelength:
            print('Error: Lengths of lists are not equal')
            return False
 
        for i in range(0, len(company_list)):
            try:
                self.buy_shares(company_list[i], number_list[i], buy_price_list[i])
            except ValueError:
                raise
            except TypeError:
                raise

    def sell_shares(self, company, number, sell_price, profit = 0):
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
        

        if self[company].is_empty():
            self._total_profit += profit
            return profit

        pop = self[company].pop()

        if pop[0] < number:
            number -= pop[0]
            profit += (pop[0]*(sell_price - pop[1]))
            return self.sell_shares(company, number, sell_price, profit)            
        elif pop[0] >= number:
            shares_left = pop[0] - number
            profit += (number*(sell_price - pop[1]))
            self[company].push([shares_left, pop[1]])
            self._total_profit += profit
            return profit
        

    def sell_multiple(self, company_list, number_list, sell_price_list):
        samelength = (len(company_list) == len(number_list) == len(sell_price_list))
        
        if not samelength:
            print('Error: Lengths of lists are not equal')
            return False
 
        for i in range(0, len(company_list)):
            try:
                self.sell_shares(company_list[i], number_list[i], sell_price_list[i])
            except ValueError:
                raise
            except TypeError:
                raise




manager = StockManager()
# manager.buy_shares("Apple", 10, 5)
# manager.buy_shares("Apple", 10, 5)
# manager.buy_shares("Apple", 10, 5)

print(manager.sell_shares('Apple', 77, 7))
print(manager.sell_shares('Apple', 29, 7))
manager.buy_shares("Apple", 10, 5)
manager.buy_shares("Apple", 10, 5)



manager.apple.print_contents()
print('net: ', manager.get_profit())
