resources = dict(money=550, water=400, milk=540, beans=120, disp_cups=9)


def remaining():
    print(f"""The coffee machine has:
{resources['water']} ml of water
{resources['milk']} ml of milk
{resources['beans']} g of coffee beans
{resources['disp_cups']} disposable cups
${resources['money']} of money""")


def espresso():
    if resources['water'] < 250:
        print("Sorry, not enough water!")
        return
    if resources['beans'] < 16:
        print("Sorry, not enough coffee beans!")
        return
    if resources['disp_cups'] < 1:
        print("Sorry, not enough disposable cups!")
        return
    else:
        resources['water'] -= 250
        resources['beans'] -= 16
        resources['disp_cups'] -= 1
        resources['money'] += 4
        print("""I have enough resources, making you a coffee!
        """)


def latte():
    if resources['water'] < 350:
        print("Sorry, not enough water!")
        return
    if resources['milk'] < 75:
        print("Sorry, not enough milk!")
        return
    if resources['beans'] < 20:
        print("Sorry, not enough coffee beans!")
        return
    if resources['disp_cups'] < 1:
        print("Sorry, not enough disposable cups!")
        return
    else:
        resources['water'] -= 350
        resources['milk'] -= 75
        resources['beans'] -= 20
        resources['disp_cups'] -= 1
        resources['money'] += 7
        print("""I have enough resources, making you a coffee!
        """)


def cappuccino():
    if resources['water'] < 200:
        print("Sorry, not enough water!")
        return
    if resources['milk'] < 100:
        print("Sorry, not enough milk!")
        return
    if resources['beans'] < 12:
        print("Sorry, not enough coffee beans!")
        return
    if resources['disp_cups'] < 1:
        print("Sorry, not enough disposable cups!")
        return
    else:
        resources['water'] -= 200
        resources['milk'] -= 100
        resources['beans'] -= 12
        resources['disp_cups'] -= 1
        resources['money'] += 6
        print("""I have enough resources, making you a coffee!
              """)


def coffee(water, milk, beans, disp_cups, money):
    coffee = input("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: 
""")
    if coffee == "1":
        return espresso()
    if coffee == "2":
        return latte()
    if coffee == "3":
        return cappuccino()
    if coffee == "back":
        return


def filling(water, milk, beans, disp_cups):
    print("Write how many ml of water you want to add:")
    resources['water'] += int(input())
    print("Write how many ml of milk you want to add:")
    resources['milk'] += int(input())
    print("Write how many grams of coffee beans you want to add:")
    resources['beans'] += int(input())
    print("Write how many disposable cups of coffee you want to add:")
    resources['disp_cups'] += int(input())


def take(money):
    print(f"I gave you ${money}")
    resources['money'] = 0
    return resources['money']


while True:
    action = input("""Write action (buy, fill, take, remaining, exit):
""")
    if action == "exit":
        break

    if action == "remaining":
        remaining()

    if action == "buy":
        coffee(resources['water'], resources['milk'], resources['beans'], resources['disp_cups'], resources['money'])

    if action == "fill":
        filling(resources['water'], resources['milk'], resources['beans'], resources['disp_cups'])

    if action == "take":
        take(resources['money'])
