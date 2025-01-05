class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money"

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == '1':
            self.make_coffee(250, 0, 16, 4)
        elif choice == '2':
            self.make_coffee(350, 75, 20, 7)
        elif choice == '3':
            self.make_coffee(200, 100, 12, 6)
        elif choice == 'back':
            return

    def make_coffee(self, water, milk,beans, money):
        if self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.money += money
            self.cups -= 1
        else:
            if self.water < water:
                print("Sorry, not enough water!")
            elif self.milk < milk:
                print("Sorry, not enough milk!")
            elif self.beans < beans:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups!")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups do you want to add:"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                print(self)
            elif action == 'exit':
                break

coffee_machine = CoffeeMachine()
coffee_machine.start()
