"""
1. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price.
"""

class Cart:
    def __init__(self):
        self.items = {}

    def add(self,name,price):
        if name in self.items:
            self.items[name] =self.items[name] + price
        else:
            self.items[name] = price

    def remove(self,name):
        if name in self.items:
            del self.items[name]

    def total(self):
        return sum(self.items.values())

cart = Cart()
while True:
    print('Choose the Options Below ')
    print('--------------------------------')
    print('1. Add item')
    print('2. Remove item')
    print('3. Show total price')
    print('4. Exit')
    choice = input('Enter your Choice : ')
    
    if choice == '1':
        name = input('Enter item name: ')
        price = float(input('Enter item price: '))
        cart.add(name,price)

    elif choice == '2':
        print(cart.items)
        name = input('Enter item name to remove: ')
        cart.remove(name)

    elif choice == '3':
        print('Total price:',cart.total())

    elif choice == '4':
        break
    else:
        print('Enter Proper Option')

#------------------------------------------------------------------------------------------------------------
'''
2. Write a Python program to create a class representing a bank.
 Include methods for managing customer accounts and transactions.

'''  

class Bank:
    def __init__(self):
        self.accounts = {}

    def create(self,acno,balance=0):
        if acno in self.accounts:
            print('Account already exists with account number:',acno)
        else:
            self.accounts[acno] = balance
            print('Account created with account number:',acno)

    def deposit(self,acno,amount):
        if acno not in self.accounts:
            print('Account not Available')
        elif amount <= 0:
            print('Enter Proper amount')
        else:
            self.accounts[acno] = self.accounts[acno] + amount
            print('Added money:',amount)
            print('New balance:',self.accounts[acno])

    def withdraw(self,acno,amount):
        if acno not in self.accounts:
            print('Account not Available')
        elif amount <= 0:
            print('Enter Proper amount')
        elif amount > self.accounts[acno]:
            print('Insufficient balance')
        else:
            self.accounts[acno] = self.accounts[acno] - amount
            print('Withdraw successful')
            print('New balance:',self.accounts[acno])

    def balance(self,acno):
        if acno not in self.accounts:
            print('Account not Available')
        else:
            print('balance:',self.accounts[acno])
b = Bank()
while True:
    print('Choose The Below Options')
    print('---------------------------------')
    print('1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Balance Check')
    print('5. Exit')

    c = input('Enter your Option : ')
    if c == '1':
        acno = input('Enter account number: ')
        balance = float(input('Enter initial balance: '))
        b.create(acno,balance)
    
    elif c == '2':
        acno = input('Enter account number: ')
        amount = float(input('Enter amount to deposit: '))
        b.deposit(acno,amount)
    
    elif c == '3':
        acno = input('Enter account number: ')
        amount = float(input('Enter amount to withdraw: '))
        b.withdraw(acno,amount)
    
    elif c == '4':
        acno = input('Enter account number: ')
        b.balance(acno)

    elif c == '5':
        print('Quitting')
        break
    else:
        print('Invalid')
