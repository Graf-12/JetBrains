x = ['_'] * 9
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
co = 0


def cell_print():
    print(f"""---------
| {x[0]} {x[1]} {x[2]} |
| {x[3]} {x[4]} {x[5]} |
| {x[6]} {x[7]} {x[8]} |
---------""")
    return


def win():
    if x[0] != "_" and x[0] == x[1] == x[2]:
        print(f"{x[0]} wins")
        return True
    elif x[3] != "_" and x[3] == x[4] == x[5]:
        print(f"{x[3]} wins")
        return True
    elif x[6] != "_" and x[6] == x[7] == x[8]:
        print(f"{x[6]} wins")
        return True
    elif x[0] != "_" and x[0] == x[3] == x[6]:
        print(f"{x[0]} wins")
        return True
    elif x[1] != "_" and x[1] == x[4] == x[7]:
        print(f"{x[1]} wins")
        return True
    elif x[2] != "_" and x[2] == x[5] == x[8]:
        print(f"{x[2]} wins")
        return True
    elif x[0] != "_" and x[0] == x[4] == x[8]:
        print(f"{x[0]} wins")
        return True
    elif x[2] != "_" and x[2] == x[4] == x[6]:
        print(f"{x[2]} wins")
        return True
    elif co == 9:
        print("Draw")
        return True


cell_print()
while True:
    c = input('Enter the coordinates: ').split()
    if c[0] not in nums or c[1] not in nums:
        print("You should enter numbers!")
    else:
        c_1 = int(c[0])
        c_2 = int(c[1])
        x = list(x)
        if c_1 < 0 or c_1 > 3 or c_2 < 0 or c_2 > 3:
            print("Coordinates should be from 1 to 3!")
        elif (c_1 and c_2 > 0) and (c_1 and c_2 < 4):
            if c_1 == 1:
                v = (c_1 - 1) + (c_2 - 1)
                if x[v] == "X" or x[v] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                if x[v] == "_":
                    if co == 0 or co == 2 or co == 4 or co == 6 or co == 8:
                        x[v] = "X"
                    else:
                        x[v] = "O"
                co += 1
                cell_print()
                if win():
                    break
            if c_1 == 2:
                v = c_1 + c_2
                if x[v] == "X" or x[v] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                if x[v] == "_":
                    if co == 0 or co == 2 or co == 4 or co == 6 or co == 8:
                        x[v] = "X"
                    else:
                        x[v] = "O"
                co += 1
                cell_print()
                if win():
                    break
            if c_1 == 3:
                v = c_1 + c_2 + 2
                if x[v] == "X" or x[v] == "O":
                    print("This cell is occupied! Choose another one!")
                    continue
                if x[v] == "_":
                    if co == 0 or co == 2 or co == 4 or co == 6 or co == 8:
                        x[v] = "X"
                    else:
                        x[v] = "O"
                co += 1
                cell_print()
                if win():
                    break
