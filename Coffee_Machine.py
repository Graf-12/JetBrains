class Machine:
    resources = dict(money=550, water=400, milk=540, beans=120, disp_cups=9)

    def remaining(self):
        print(f"""The coffee machine has:
    {Machine.resources['water']} ml of water
    {Machine.resources['milk']} ml of milk
    {Machine.resources['beans']} g of coffee beans
    {Machine.resources['disp_cups']} disposable cups
    ${Machine.resources['money']} of money""")

    def espresso(self):
        if Machine.resources['water'] < 250:
            print("Sorry, not enough water!")
            return
        if Machine.resources['beans'] < 16:
            print("Sorry, not enough coffee beans!")
            return
        if Machine.resources['disp_cups'] < 1:
            print("Sorry, not enough disposable cups!")
            return
        else:
            Machine.resources['water'] -= 250
            Machine.resources['beans'] -= 16
            Machine.resources['disp_cups'] -= 1
            Machine.resources['money'] += 4
            print("""I have enough resources, making you a coffee!
""")

    def latte(self):
        if Machine.resources['water'] < 350:
            print("Sorry, not enough water!")
            return
        if Machine.resources['milk'] < 75:
            print("Sorry, not enough milk!")
            return
        if Machine.resources['beans'] < 20:
            print("Sorry, not enough coffee beans!")
            return
        if Machine.resources['disp_cups'] < 1:
            print("Sorry, not enough disposable cups!")
            return
        else:
            Machine.resources['water'] -= 350
            Machine.resources['milk'] -= 75
            Machine.resources['beans'] -= 20
            Machine.resources['disp_cups'] -= 1
            Machine.resources['money'] += 7
            print("""I have enough resources, making you a coffee!
            """)

    def cappuccino(self):
        if Machine.resources['water'] < 200:
            print("Sorry, not enough water!")
            return
        if Machine.resources['milk'] < 100:
            print("Sorry, not enough milk!")
            return
        if Machine.resources['beans'] < 12:
            print("Sorry, not enough coffee beans!")
            return
        if Machine.resources['disp_cups'] < 1:
            print("Sorry, not enough disposable cups!")
            return
        else:
            Machine.resources['water'] -= 200
            Machine.resources['milk'] -= 100
            Machine.resources['beans'] -= 12
            Machine.resources['disp_cups'] -= 1
            Machine.resources['money'] += 6
            print("""I have enough resources, making you a coffee!
""")

    def coffee(self, water, milk, beans, disp_cups, money):
        coffee = input("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: 
""")
        if coffee == "1":
            return Machine.espresso(self)
        if coffee == "2":
            return Machine.latte(self)
        if coffee == "3":
            return Machine.cappuccino(self)
        if coffee == "back":
            return

    def filling(self, water, milk, beans, disp_cups):
        print("Write how many ml of water you want to add:")
        Machine.resources['water'] += int(input())
        print("Write how many ml of milk you want to add:")
        Machine.resources['milk'] += int(input())
        print("Write how many grams of coffee beans you want to add:")
        Machine.resources['beans'] += int(input())
        print("Write how many disposable cups of coffee you want to add:")
        Machine.resources['disp_cups'] += int(input())

    def take(self, money):
        print(f"I gave you ${money}")
        Machine.resources['money'] = 0
        return Machine.resources['money']

    def menu(self):
        while 1:
            action = input("""Write action (buy, fill, take, remaining, exit):
""")
            if action == "exit":
                break

            if action == "remaining":
                Machine.remaining(self)
                return Machine.menu(self)

            if action == "buy":
                Machine.coffee(self, Machine.resources['water'], Machine.resources['milk'], Machine.resources['beans'],
                               Machine.resources['disp_cups'], Machine.resources['money'])
                return Machine.menu(self)

            if action == "fill":
                Machine.filling(self, Machine.resources['water'], Machine.resources['milk'], Machine.resources['beans'],
                                Machine.resources['disp_cups'])
                return Machine.menu(self)

            if action == "take":
                Machine.take(self, Machine.resources["money"])
                return Machine.menu(self)


coffee_machine = Machine()
coffee_machine.menu()
