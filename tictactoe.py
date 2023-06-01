class tictactoe:
    def __init__(self):
        self.location1 = 0
        self.location2 = 0

    def getdata(self):
        self.location1 = int(input("enter location 1(row):"))
        self.location2 = int(input("enter location 2(column):"))
        if ((self.location1<0 or self.location1>=3) or (self.location2<0 or self.location2>=3) or list[self.location1][self.location2] == 1 or list[self.location1][self.location2] == 2):
            return "select another"
        else:
            return "you can proceed"

        # print(list[0][0])


turn = 1
list = []
list1 = [0, 0, 0]
list.append(list1)
list2 = [0, 0, 0]
list.append(list2)
list3 = [0, 0, 0]
list.append(list3)
flagr1 = 0
flagr2 = 0
flagr3 = 0
flagc1 = 10
flagc2 = 10
flagc3 = 10
dleft = 0
dright = 0
game = 0
game1 = 0
flagrr1 = 0
flagrr2 = 0
flagrr3 = 0
flagcc1 = 10
flagcc2 = 10
flagcc3 = 10
ddleft = 0
ddright = 0
flag = 0
ob1 = tictactoe()
ob2 = tictactoe()
print("***********************Welcome to online Tic-Tac-Toe player***********************")
print("Are you ready to start the game?")
choice = input()
if (choice == 'y'):
    print("player 1: you are alloted with mark 1")
    print("player 2: you are alloted with mark 2")
    print("All the best!!")
    print("original grid looks like:")
    print(list[0], end="")
    print("\n")
    print(list[1], end="")
    print("\n")
    print(list[2], end="")
    print("\n")
    while (turn <= 9 and game1 == 0 and game == 0):
        print("***********************player 1 turn***********************")
        res1 = ob1.getdata()
        while (res1 == "select another"):
            res1 = ob1.getdata()
        if (res1 == "you can proceed"):
            pass
        for i in range(3):
            for j in range(3):
                if ((i == ob1.location1) and (j == ob1.location2)):
                    list[i][j] = 1
                    print(list[0], end="")
                    print("\n")
                    print(list[1], end="")
                    print("\n")
                    print(list[2], end="")
                    print("\n")
                    if ((i == 0) or (i == 1) or (i == 2) or (j == 0) or (j == 1) or j == 2 or i == j or (
                            ((i == 0) and (j == 2)) or ((i == 1) and (j == 1)) or ((i == 2) and (j == 0)))):
                        if (i == 0):
                            if (list[i][j] == 1):
                                flagr1 += 1
                                flagc1 = j


                        elif (i == 1):
                            if (list[i][j] == 1):
                                flagr2 += 1
                                flagc2 = j
                        elif (i == 2):
                            if (list[i][j] == 1):
                                flagr3 += 1
                                flagc3 = j

                        if (i == j):
                            if (list[i][j] == 1):
                                dleft += 1

                        if (((i == 0) and (j == 2)) or ((i == 1) and (j == 1)) or ((i == 2) and (j == 0))):
                            if (list[i][j] == 1):
                                dright += 1
        if ((flagc1 == flagc2) and (flagc2 == flagc3) and (flagc1 == flagc3)):
            print("*********************** player 1 wins ***********************")
            game = 1
        elif (flagr1 == 3 or flagr2 == 3 or flagr3 == 3 or dleft == 3 or dright == 3):
            print("*********************** player 1 wins ***********************")
            game = 1
        elif (turn == 9):
            print("*********************** tie ***********************")
            break
        turn += 1
        if (turn <= 8 and game == 0 and game1 == 0):
            print("***********************player 2 turn***********************")
            res1=ob2.getdata()
            while (res1 == "select another"):
                res1 = ob2.getdata()
            if (res1 == "you can proceed"):
                pass
            for i in range(3):
                for j in range(3):
                    if ((i == ob2.location1) and (j == ob2.location2)):
                        list[i][j] = 2
                        print(list[0], end="")
                        print("\n")
                        print(list[1], end="")
                        print("\n")
                        print(list[2], end="")
                        print("\n")
                        if ((i == 0) or (i == 1) or (i == 2) or (j == 0) or (j == 1) or j == 2 or i == j or (
                                ((i == 0) and (j == 2)) or ((i == 1) and (j == 1)) or ((i == 2) and (j == 0)))):
                            if (i == 0):
                                if (list[i][j] == 2):
                                    flagrr1 += 1
                                    flagcc1 = j


                            elif (i == 1):
                                if (list[i][j] == 2):
                                    flagrr2 += 1
                                    flagcc2 = j
                            elif (i == 2):
                                if (list[i][j] == 2):
                                    flagrr3 += 1
                                    flagcc3 = j

                            if (i == j):
                                if (list[i][j] == 2):
                                    ddleft += 1

                            if (((i == 0) and (j == 2)) or ((i == 1) and (j == 1)) or ((i == 2) and (j == 0))):
                                if (list[i][j] == 2):
                                    ddright += 1
            if ((flagcc1 == flagcc2) and (flagcc2 == flagcc3) and (flagcc1 == flagcc3)):
                print("*********************** player 2 wins ***********************")
                game = 1
            elif (flagrr1 == 3 or flagrr2 == 3 or flagrr3 == 3 or ddleft == 3 or ddright == 3):
                print("*********************** player 2 wins ***********************")
                game = 1
            turn+=1
else:
    print("have a good day!!!")
