import threading

class BankAccount:
    def __init__(self):
        self._is_active = False
        self._balance = 0
        self._mutex = threading.Lock()

        

    def get_balance(self):
        while self._mutex.locked:
            continue
        return self._balance

    def open(self):
        if self._is_active == True:
            raise ValueError('account already open')
        self._is_active = True

    def deposit(self, amount):
        # prevent deposit to non-active account
        if not self._is_active:
            raise ValueError('account has not been opened')
        # wait until balance is unlocked
        while self._mutex.locked:
            continue
         # acquire mutex to prevent simultaneous access
        self._mutex.acquire()
        self._balance += amount
        self._mutex.release()

    def withdraw(self, amount):
        # prevent withdrawal from non-active account
        if not self._is_active:
            raise ValueError('account has not been opened')
        
        while self._mutex.locked:
            continue

        

    def close(self):
        pass
