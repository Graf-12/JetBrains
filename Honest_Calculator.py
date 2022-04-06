msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
ope = ["+", "-", "*", "/"]
memory = 0
result = 0


def check(x, y, op):
    msg = ""
    if (x.is_integer() and 10 > x > -10) and (y.is_integer() and 10 > y > -10):
        msg = msg + msg_6
    if x == 1 and op == "*" or y == 1 and op == "*":
        msg = msg + msg_7
    if (x == 0 and (op == "*" or op == "+" or op == "-")) or (y == 0 and (op == "*" or op == "+" or op == "-")):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    x, op, y = input().split()
    if x == "M" and y == "M":
        x = float(memory)
        y = float(memory)
    if x == "M":
        x = float(memory)
        try:
            y = float(y)
        except ValueError:
            print(msg_1)
            continue
    if y == "M":
        y = float(memory)
        try:
            x = float(x)
        except ValueError:
            print(msg_1)
            continue
    else:
        try:
            x, y = float(x), float(y)
        except ValueError:
            print(msg_1)
            continue
    check(x, y, op)
    if op not in ope:
        print(msg_2)
        continue
    if op == "+":
        result = x + y
        print(result)
    if op == "-":
        result = x - y
        print(x - y)
    if op == "*":
        result = x * y
        print(x * y)
    if op == "/" and y != 0:
        result = x / y
        print(x / y)
    elif op == "/" and y == 0:
        print(msg_3)
        continue

    print(msg_4)
    answer = input()
    if answer == "y":
        if result % 1 == 0 and 10 > result > -10:
            print(msg_10)
            ans = input()
            if ans == "y":
                print(msg_11)
                ans = input()
                if ans == "y":
                    print(msg_12)
                    ans = input()
                    if ans == "y":
                        memory = result
        else:
            memory = result
        print(msg_5)
        continue_ = input()
        if continue_ == "y":
            continue
        if continue_ == "n":
            break
    else:
        print(msg_5)
        continue_ = input()
        if continue_ == "y":
            continue
        else:
            break
