class BankAccount:
    def __init__(self, balance, owner=None):
        balance = float(balance)
        if not BankAccount.is_valid_amount(balance):
            raise ValueError("Inform a valid amount.")
        self.__balance = (balance)         
        self.owner = str(owner).strip()

    def __str__(self):
        return f"BankAccount of {self.owner} with balance: £{self.__balance:.2f}"
    
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"
        
    @property
    def balance(self):
        return self.__balance;

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Cannot set a negative value!")
        else:
            self.__balance = value

    @classmethod
    def from_string(cls, data_str):
        ownr, bal = str(data_str).split(":")
        return cls(float(bal), ownr)

    @staticmethod
    def is_valid_amount(value):
        return isinstance(value, (int,float)) and value >=0


p = BankAccount(85, 'Pimpim')
#print(p)
#print(repr(p))