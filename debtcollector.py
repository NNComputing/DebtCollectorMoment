# Debt Calculator for the interested debt collectors
# Feel free to change variable names and values to your preference

def calculate_debt(a, b, c): # a, b and c are individual prices of certain things
    # add more arguments as necessary (if you need to work with more prices)
    a_nums = int(input(f'How many times has your debtor not paid for something of price ${a:.2f}?: ')) # number of times you paid price a
    b_nums = int(input(f'How many times has your debtor not paid for something of price ${b:.2f}?: ')) # number of times you paid price b
    c_nums = int(input(f'How many times has your debtor not paid for something of price ${c:.2f}?: ')) # number of times you paid price c
    # remember to add d_nums, etc. for more prices
    debt = (a_nums * a) + (b_nums * b) + (c_nums * c) # sum of debt (remember to add d_nums, etc. for more prices)
    print(f'The debt owed by this person is ${debt:.2f}')

# main
calculate_debt(3.40, 3.80, 1.00) # sample values a = 3.40, b = 3.80, c = 1.00, a_nums = 10, b_nums = 6, c_nums = 11



#### BY NAVIN AMAL ANAND OF ASRJC CLASS 24/12 ####
