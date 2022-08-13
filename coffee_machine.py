water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
income = 550


class CoffeeMachine:   # creating the class
    def check_availability(self, order): 
        if order == "1":
            if self.water >= 250 and self.coffee_beans >= 16:
                return True
            else:
                return False
        elif order == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                return True
            else:
                return False
        else:
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                return True
            else:
                return False
                
    def find_default(self, order):
        if order == "1":
            if self.water <= 250:
                print("Sorry, not enough water!")
            if self.coffee_beans <= 16:
                print("Sorry, not enough coffee beans!")
        elif order == "2":
            if self.water <= 350:
                print("Sorry, not enough water!")
            if self.milk <= 75:
                print("Sorry, not enough milk!")
            if self.coffee_beans <= 20:
                print("Sorry, not enough coffee beans!")
        else:
            if self.water <= 200:
                print("Sorry, not enough water!")
            if self.milk <= 100:
                print("Sorry, not enough milk!")
            if self.coffee_beans <= 12:
                print("Sorry, not enough coffee beans!")
                
    def take(self):
        print(f"I gave you ${income}")
        self.income = 0
    
    def fill(self):            # Restock the resource
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups you want to add:\n"))

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        order = input()
        if order == "back":
            pass
        else:
            can_order = self.check_availability(order)
            if can_order and self.disposable_cups >= 1:  # Make the coffee
                print("I have enough resources, making you a coffee!")
                if order == "1":
                    self.water -= 250
                    self.coffee_beans -= 16
                    self.income += 4
                    self.disposable_cups -= 1
                elif order == "2":
                    self.water -= 350
                    self.milk -= 75
                    self.coffee_beans -= 20
                    self.income += 7
                    self.disposable_cups -= 1
                else:
                    self.water -= 200
                    self.milk -= 100
                    self.coffee_beans -= 12
                    self.income += 6
                    self.disposable_cups -= 1
            elif can_order is False and self.disposable_cups >= 1:
                self.find_default(order)
            elif self.disposable_cups == 0:
                print("Sorry, not enough disposable cups!")
        
    def machine_status(self, water, milk, coffee_beans, disposable_cups, income):
        print("The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans} g of coffee beans")
        print(f"{self.disposable_cups} disposable cups")
        print(f"${self.income} of money")   

    def __init__(self, water, milk, coffee_beans, disposable_cups, income):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.income = income
        operation = input("Write action (buy, fill, take, remaining, exit):")
        while operation != "exit":
            self.engage(operation)
            operation = input("Write action (buy, fill, take, remaining, exit):")
    
    def engage(self, operation):
        if operation == "buy":
            self.buy()
        elif operation == "fill":
            self.fill()
        elif operation == "take":
            self.take()
        else:
            self.machine_status(self.water, self.milk, self.coffee_beans, self.disposable_cups, self.income)


Coffee_Machine = CoffeeMachine(water, milk, coffee_beans, disposable_cups, income)
