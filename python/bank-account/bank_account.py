import threading
from typing import ValuesView

class BankAccount:
    def __init__(self) -> None:
        self._is_active: bool = False
        self._balance: float = 0
        self._mutex = threading.Lock()    

    def get_balance(self) -> float:
        # first allow ongoing transactions to finish
          with self._mutex:
            # closed account does not have a balance
            # access should be denied
            if not self._is_active:
                raise ValueError('account is closed')
            return self._balance
      
     


    def open(self) -> None:
        # use mutex to prevent simultaneous modificatoins
        with self._mutex:
            # prevent opening a new bank account
            if self._is_active:
                raise ValueError('account already open')
            # initialize balance with zero value
            # this should already be performed in 'init' and 'close'
            # however, you cannot be too careful
            self._balance = 0
            # open the bank account
            self._is_active = True

    def deposit(self, amount) -> None:
        # use mutex to prevent simultaneous modifications
        with self._mutex:
            # prevent deposit to non-active account
            if not self._is_active:
                raise ValueError('account has not been opened')
            # prevent non-negative deposits 
            if amount < 0:
                raise ValueError('cannout deposit negative amount')
            self._balance += amount

    def withdraw(self, amount):
        # use mutex to prevent simultaneous modifications
        with self._mutex:
             # prevent withdrawal from non-active account
            if not self._is_active:
                raise ValueError('account has not been opened')
            # prevent non-negative withdrawals
            if amount < 0:
                raise ValueError('cannot withdraw negative amount')
            # prevent over-withdrawal
            if self._balance < amount:
                raise ValueError('you do not have enough money in the account')
            # successfully withdraw if no errors are raised
            self._balance -= amount
     
    def close(self):
        # first finish all transactions before closing the account
        with self._mutex:
            # check if the balance is already closed
            if not self._is_active:
                raise ValueError('account is already closed')
            # clear the account balance
            self._balance = 0
            # close the account
            self._is_active = False
        

""" 
I have a question:
I tried to use the following:
    
    while self._mutex.locked():
            continue    
    self._mutex.acquire()
    if not self._is_active:
        raise ValueError()
    return self._balance <------- does returning before releasing the mutex 
    self._mutex.release()         cause a problem
    
    
    This causes the program to raise an error on test no. 9
    Replacing it with this 

    
    def get_balance(self) -> float:
          with self._mutex:
            if not self._is_active:
                raise ValueError('account is closed')
            return self._balance
    
    solves the issue

    I would be very grateful if you could tell me why this happens
      
"""