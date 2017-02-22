
# bank.py

# Problem 1

class Account(object):

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'insufficient funds'

    def deposit(self, amount):        # pre: amount >= 0
        self.balance += amount
        return self.balance

    def show(self):
        return self.balance

'''
>>> acc = Account(100)
>>> acc.withdraw(75)
25
>>> acc.withdraw(50)
'insufficient funds'
>>> acc.deposit(40)
65
>>> acc.withdraw(35)
30
>>> acc.show()
30
'''

# Problem 2

class Accumulator(object):

    def __init__(self, n):
        self.counter = n

    def incr(self, amount):
        self.counter += amount
        return self.counter

'''
>>> a = Accumulator(5)
>>> a.incr(10)
15
>>> a.incr(10)
25
'''

# Problem 3

class Account(object):

    def __init__(self, balance, password):
        self.balance = balance
        self.password = password

    def withdraw(self, amount, password):
        if self.password != password:
            return 'incorrect password'
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'insufficient funds'

    def deposit(self, amount, password):        # pre: amount >= 0
        if self.password != password:
            return 'incorrect password'
        self.balance += amount
        return self.balance

    def show(self, password):
        if self.password != password:
            return 'incorrect password'
        return self.balance

'''
>>> acc = Account(100, 'secret password')
>>> acc.withdraw(40, 'secret password')
60
>>> acc.withdraw(50, 'some other password')
'incorrect password'
'''

# Problem 4

def call_the_cops():
    raise Exception('Processing your request, please wait ...')

class Account(object):

    def __init__(self, balance, password):
        self.attempts = 0        # number of incorrect password attempts
        self.balance = balance
        self.password = password

    def password_okay(self, password):
        if self.password != password or self.attempts >= 3:
            self.attempts += 1
            if self.attempts >= 3:
                call_the_cops()   # throws an exception
            else:
                return False
        else:
            self.attempts = 0
            return True

    def withdraw(self, amount, password):
        if not self.password_okay(password):
            return 'incorrect password'
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'insufficient funds'

    def deposit(self, amount, password):        # pre: amount >= 0
        if not self.password_okay(password):
            return 'incorrect password'
        self.balance += amount
        return self.balance

    def show(self, password):
        if not self.password_okay(password):
            return 'incorrect password'
        return self.balance

'''
>>> acc = Account(100, 'secret password')
>>> acc.withdraw(40, 'secret password')
60
>>> acc.withdraw(50, 'some other password')
'incorrect password'
>>> acc.withdraw(50, 'some other password')
'incorrect password'
>>> acc.withdraw(50, 'secret password')
10
>>> acc.withdraw(50, 'some other password')
'incorrect password'
>>> acc.withdraw(50, 'some other password')
'incorrect password'
>>> acc.withdraw(50, 'some other password')
...
Exception: Processing your request, please wait ...
>>> acc.withdraw(50, 'some other password')
...
Exception: Processing your request, please wait ...
>>> acc.withdraw(50, 'secret password')
...
Exception: Processing your request, please wait ...
'''
