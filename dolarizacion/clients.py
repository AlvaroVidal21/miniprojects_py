BANKS = ['BCP', 'INTERBANK', 'SCOTIABANK', 'BBVA']
#           0          1            2          3

class BankingClients:
    def __init__(self, name, amount, bank=0): # bank for default is BCP
        self.name = name
        self.amount = amount
        self.bank = BANKS[bank]