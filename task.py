class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.dollars += (self.cents + deposit_cents) // 100
        self.cents = (self.cents + deposit_cents) % 100

        print(self.dollars, self.cents)


transfer = PiggyBank(1, 2)

transfer.add_money(500, 98)
