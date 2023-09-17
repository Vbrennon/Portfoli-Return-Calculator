#
# Brennon Villacarlos
# Start: 2/24/2023
# Current: 9/17/2023
#

# import relevant packages
from time import sleep
import yfinance as yf


def main():
    # create 2 while loops for input validation
    print("Hello, this program calculates long-term returns on your portfolio.\n"
          "This calculation can extend any amount of years and contain any number of stocks\n"
          "This calculation assumes no changes in dividend yield over time and the stock's\n"
          "average annual return will remain constant over the years.\n")
    print('\nThese assumptions are certainly false.\n')
    print('\nEnjoy!\n')
    while True:
        # ask user how many years to invest and how many stocks they want to invest in.
        try:
            tick_num = int(input('How many tickers would you like in your portfolio? '))
            years = int(input('How many years would you like to invest? '))
            break
        except ValueError:
            print('\nOnly whole numbers, please\n')

    while True:
        # get tickers from user and ask for monthly deposit
        try:
            monthly_deposit = int(input('How much would you like to deposit a month? '))
            yearly_deposit = monthly_deposit * 12
            break
        except:
            print('\nRound to the nearest whole dollar, do not put any commas,'
                  '\nand make sure you only enter integers.\n')

    # iterate through tickers and calculate yearly gain
    total_return = 0
    total_div = 0
    for i in range(tick_num):
        stock = Stock(tick_num, yearly_deposit, years)
        (annual_return, div_agg) = stock.calculate_total()
        total_div += div_agg
        total_return += annual_return

    # print end statement
    print(
        f'\nIf you deposited ${yearly_deposit:.2f} yearly over a period of {years} year(s),\n'
        f'your account total would be ${int(total_return)}. Annually, you would receive ${total_div:.2f} '
        f'in dividends. \n\n*Note: this does DRIP')

    # Add this in at the arrow later when you complete: Annually, you would receive ${total_div:.2f} ' f'in dividends.


class Stock:
    # two while loops for input validation
    def __init__(self, tick_num, yearly_deposit, years):
        while True:
            try:
                self.years = years
                # ask for ticker
                self.ticker = input('\nPlease enter a ticker. ')

                # pull yahoo data for 1 year
                self.data_year = yf.Ticker(self.ticker).history(period='1y')

                # pull yahoo data for entire history
                self.data_max = yf.Ticker(self.ticker).history(period='max')

                # get last quote
                self.last_quote = self.data_year['Close'].iloc[-1]

                # get dividend data
                self.div_per_share = self.data_year['Dividends'].sum()

                # warn user if stock does not have dividends.
                if self.div_per_share <= 0:
                    print("\nJust so you know, this stock doesn't have dividends", end='')
                    for i in range(3):
                        print('.', end='')
                        sleep(1)
                    print(f"\n\n{self.ticker.upper()}'s closing price was ${self.last_quote:.2f}")
                    break
                # else print the tickers last quote and the dividend amount per share
                else:
                    print(f"\n{self.ticker.upper()}'s closing price was ${self.last_quote:.2f}, giving "
                          f"${self.div_per_share:.2f} per share annually.")
                    break

            except:
                print('\nPlease check for typos when entering ticker\n')

        while True:
            # ask user for what percentage of their portfolio to contribute to this stock
            # if they only wanted 1 ticker in their portfolio it sets self.percent to 100
            try:
                if tick_num > 1:
                    self.percent = int(input('\nWhat percentage of your portfolio would you like this stock to be? '))
                    self.portion = (self.percent / 100) * yearly_deposit
                    break

                else:
                    self.percent = 100
                    self.portion = (self.percent / 100) * yearly_deposit
                    break
            except:
                print('\nOnly integers, please. (no percent signs)\n')

    def calculate_avg_return(self):
        # creates dictionary where each key is a year and corresponding value is a dataframe
        # with all the stock information for that year
        yearly_data = {}
        for year in range(self.data_max.index.min().year, self.data_max.index.max().year + 1):
            yearly_data[year] = self.data_max[self.data_max.index.year == year]
        # use list comprehension to iterate through yearly_data and then
        # calculate the annual return for each year and append them to returns list
        returns = [(yearly_data[year]['Close'].iloc[-1] - yearly_data[year]['Open'].iloc[0]) /
                   yearly_data[year]['Open'].iloc[0] for year in yearly_data.keys()]
        # average the list of annual returns
        avg_return = sum(returns) / len(returns)
        return avg_return

    # calculates the total gain over time for this particular stock
    # takes the years user wants to invest, how much they would like to invest a year,
    # and then uses a for loop to iterate in the range of years calculating the yearly gain
    # and appending it to the total variable
    def calculate_total(self):
        total = 0
        num_shares = 0
        for i in range(self.years):
            total += self.portion
            if i > 0:
                self.last_quote += self.last_quote * self.calculate_avg_return()
            else:
                pass
            num_shares += self.portion / self.last_quote
            div_gain = total / self.last_quote * self.div_per_share
            num_shares += div_gain / self.last_quote
            total += div_gain
            add_return = total * self.calculate_avg_return()
            num_shares += add_return / self.last_quote
            total += add_return
            div_agg = num_shares * self.div_per_share
        return total, div_agg


main()
