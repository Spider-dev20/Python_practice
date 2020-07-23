class Game:
    money = int(input())

    def __init__(self, price, name, plural):
        self.price = price
        self.name = name
        self.plural = plural
        self.calculation = Game.money // price


    def animal(self):
        if self.calculation == 1:
            print(self.calculation, self.name)
        else:
            print(self.calculation, self.plural)


chicken = Game(23, "chicken", "chickens")
goat = Game(678, "goat", "goats")
pig = Game(1296, "pig", "pigs")
cow = Game(3848, "cow", "cows")
sheep = Game(6769, "sheep", "sheep")


if Game.money >= 6769:
    sheep.animal()
elif Game.money >= 3848:
    cow.animal()
elif Game.money >= 1296:
    pig.animal()
elif Game.money >= 678:
    goat.animal()
elif Game.money >= 23:
    chicken.animal()
else:
    print("None")
