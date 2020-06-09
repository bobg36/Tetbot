from PIL import ImageGrab
import os
import time
import win32api
import win32con
import keyPress
import quickGrab
import functions

initPix = (720, 28)  # pixel of piece when it first appears

# rgb values of the pieces
Oc = (252, 212, 50)
Lc = (252, 127, 50)
Jc = (96, 69, 228)
Ic = (48, 251, 177)
Tc = (228, 69, 212)
Sc = (176, 252, 50)
Zc = (253, 52, 63)

# boardState[column][row], 1 has block, 0 is empty
boardState = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 9
]

# column height, position of highest block, blind to holes
colh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# counting distribution of rotations for debugging
O1 = 0
I1 = 1
I2 = 2
L1 = 3
L2 = 4
L3 = 5
L4 = 6
J1 = 7
J2 = 8
J3 = 9
J4 = 10
T1 = 11
T2 = 12
T3 = 13
T4 = 14
Z1 = 15
Z2 = 16
S1 = 17
S2 = 18
CLEAR = 19
distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def main():
    repeat = 0
    keyPress.waitStart()
    while repeat < 99999999:
        1
        nextPiece = (0, 0, 0)
        im = quickGrab.screenGrab()
        nextPiece = im.getpixel(initPix)
        time.sleep(0.01)
        if(nextPiece == Oc):
            print('Oc')
            compareO()
        if(nextPiece == Lc):
            print('Lc')
            compareL()
        if(nextPiece == Jc):
            print('Jc')
            compareJ()
        if(nextPiece == Ic):
            print('Ic')
            compareI()
        if(nextPiece == Tc):
            print('Tc')
            compareT()
        if(nextPiece == Sc):
            print('Sc')
            compareS()
        if(nextPiece == Zc):
            print('Zc')
            compareZ()
        print('distribution:' + str(distribution) +
              '      Column Height: ' + str(colh))
        checkClear()
        updateColh()
        # print(distribution)
        # print(colh)


def checkClear():  # checks for line clear if row is full
    row = 0
    while row <= 20:
        count = 0
        col = 0
        while col <= 9:
            if boardState[col][row] == 1:
                count = count + 1
            col = col + 1
        if count == 10:
            clearRow(row)
            distribution[CLEAR] = distribution[CLEAR] + 1
            row = row-1
        row = row + 1


def clearRow(row):  # clears row, copies the row above
    while row <= 23:
        col = 0
        while col <= 9:
            boardState[col][row] = boardState[col][row+1]
            col = col + 1
        row = row + 1


def updateColh():  # updates column height array
    i = 0
    while i <= 9:  # for each column
        highest = 0
        j = 0
        while j <= 19:
            if boardState[i][j] == 1:
                highest = j
            j = j + 1
        colh[i] = highest
        i = i + 1


def heightDiff(mult):  # 2nd heuristic to stack lower
    sum = 0
    i = 0
    while i <= 8:
        sum = sum + abs(colh[i] - colh[i+1])
        i = i + 1
        if i > 18:
            i = i + 5
    sum = sum*mult
    return sum

# functions to compare positions of each piece and then place them


def compareI():
    rotation = 2
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1, DEFAULT ROTATION AT THE END, LAST = HIGHER PRIORITY!
    Irot1 = compareI1()
    Irot2 = compareI2()

    i = 0
    while i <= 6:  # rotation 1

        if Irot1[i] <= lowest:
            lowest = Irot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 9:  # rotation 2
        if Irot2[i] <= lowest:
            lowest = Irot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

        # j = 0
        # lowesth = 999999
        # while j <= 9:
        #     if colh[j] <= lowesth:
        #         lowesth = colh[j]
        #         lowesthIndex = j
        #     j = j + 1

    if rotation == 1:
        distribution[I1] = distribution[I1] + 1
        functions.placePiece4(lowestIndex)
        highest = getHighest4(lowestIndex)
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex+1][highest+1] = 1
        boardState[lowestIndex+2][highest+1] = 1
        boardState[lowestIndex+3][highest+1] = 1

    if rotation == 2:
        distribution[I2] = distribution[I2] + 1
        keyPress.moveUp()
        functions.placePiece1(lowestIndex)
        highest = colh[lowestIndex]
        boardState[lowestIndex][highest+4] = 1
        boardState[lowestIndex][highest+3] = 1
        boardState[lowestIndex][highest+2] = 1
        boardState[lowestIndex][highest+1] = 1


def compareI2():
    # 1
    # 1
    # 1
    # 1
    list = []
    i = 0
    while i <= 9:
        temp = colh[i]
        colh[i] = colh[i] + 4
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp
        i = i + 1
        list.append(Sum)
    return list


def compareI1():
    # 1 1 1 1
    list = []
    i = 0
    while i <= 6:
        highest = getHighest4(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        temp4 = colh[i+3]
        colh[i] = highest + 1
        colh[i+1] = highest + 1
        colh[i+2] = highest + 1
        colh[i+3] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        colh[i+3] = temp4
        i = i + 1
        list.append(Sum)
    return list


def compareL():
    rotation = 1
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Lrot1 = compareL1()
    Lrot2 = compareL2()
    Lrot3 = compareL3()
    Lrot4 = compareL4()

    i = 0
    while i <= 8:  # LOWEST PRIORITY!
        if Lrot2[i] <= lowest:
            lowest = Lrot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

    i = 0
    while i <= 7:
        if Lrot1[i] <= lowest:
            lowest = Lrot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 7:
        if Lrot3[i] <= lowest:
            lowest = Lrot3[i]
            lowestIndex = i
            rotation = 3
        i = i + 1

    i = 0
    while i <= 8:
        if Lrot4[i] <= lowest:
            lowest = Lrot4[i]
            lowestIndex = i
            rotation = 4
        i = i + 1

    if rotation == 1:
        distribution[L1] = distribution[L1] + 1
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex+1][highest+1] = 1
        boardState[lowestIndex+2][highest+1] = 1
        boardState[lowestIndex+2][highest+2] = 1

    if rotation == 2:
        distribution[L2] = distribution[L2] + 1
        keyPress.moveUp()
        functions.placePiece2(lowestIndex)
        highest = getHighest2(lowestIndex)
        boardState[lowestIndex][highest+3] = 1
        boardState[lowestIndex][highest+2] = 1
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex+1][highest+1] = 1

    if rotation == 3:
        distribution[L3] = distribution[L3] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        if colh[lowestIndex] >= colh[lowestIndex + 1] and colh[lowestIndex] >= colh[lowestIndex+2]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+2][highest+2] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+2][highest+1] = 1

    if rotation == 4:
        distribution[L4] = distribution[L4] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        keyPress.moveUp()
        functions.placePiece2b(lowestIndex)
        highest = getHighest2(lowestIndex)
        if colh[lowestIndex+1] >= colh[lowestIndex]:
            boardState[lowestIndex][highest+3] = 1
            boardState[lowestIndex+1][highest+3] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
        elif colh[lowestIndex+1]+1 >= colh[lowestIndex]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
            boardState[lowestIndex+1][highest-1] = 1


def compareL1():
    #     2
    # 1 1 2
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        colh[i] = highest + 1
        colh[i+1] = highest + 1
        colh[i+2] = highest + 2
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareL2():

    # 3
    # 3
    # 3 1
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        colh[i] = highest + 3
        colh[i+1] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareL3():
    # 2 2 2
    # 2
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        if colh[i] >= colh[i+1] and colh[i] >= colh[i+2]:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
            colh[i+2] = highest + 2
        else:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
            colh[i+2] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareL4():
    # 3 3
    #   3
    #   3
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i] > colh[i+1] + 1:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
        elif colh[i] > colh[i+1]:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
        else:
            colh[i] = highest + 3
            colh[i+1] = highest + 3
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareJ():
    rotation = 1
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Jrot1 = compareJ1()
    Jrot2 = compareJ2()
    Jrot3 = compareJ3()
    Jrot4 = compareJ4()

    i = 0
    while i <= 8:
        if Jrot4[i] <= lowest:
            lowest = Jrot4[i]
            lowestIndex = i
            rotation = 4
        i = i + 1

    i = 0
    while i <= 7:
        if Jrot1[i] <= lowest:
            lowest = Jrot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 7:
        if Jrot3[i] <= lowest:
            lowest = Jrot3[i]
            lowestIndex = i
            rotation = 3
        i = i + 1

    i = 0
    while i <= 8:
        if Jrot2[i] <= lowest:
            lowest = Jrot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

    if rotation == 1:
        distribution[J1] = distribution[J1] + 1
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex][highest+2] = 1
        boardState[lowestIndex+1][highest+1] = 1
        boardState[lowestIndex+2][highest+1] = 1

    if rotation == 2:
        distribution[J2] = distribution[J2] + 1
        keyPress.moveUp()
        functions.placePiece2(lowestIndex)
        highest = getHighest2(lowestIndex)
        if colh[lowestIndex] >= colh[lowestIndex + 1]:
            boardState[lowestIndex][highest+3] = 1
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+3] = 1
        elif colh[lowestIndex]+1 >= colh[lowestIndex + 1]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex+1][highest+2] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex][highest-1] = 1
            boardState[lowestIndex+1][highest+1] = 1

    if rotation == 3:
        distribution[J3] = distribution[J3] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        if colh[lowestIndex+2] >= colh[lowestIndex + 1] and colh[lowestIndex+2] >= colh[lowestIndex]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+2][highest+2] = 1
            boardState[lowestIndex+2][highest+1] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+2][highest+1] = 1
            boardState[lowestIndex+2][highest] = 1

    if rotation == 4:
        distribution[J4] = distribution[J4] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        keyPress.moveUp()
        functions.placePiece2b(lowestIndex)
        highest = getHighest2(lowestIndex)
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex+1][highest+1] = 1
        boardState[lowestIndex+1][highest+2] = 1
        boardState[lowestIndex+1][highest+3] = 1


def compareJ1():
    # 2
    # 2 1 1
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        colh[i] = highest + 2
        colh[i+1] = highest + 1
        colh[i+2] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareJ2():
    # 3 3
    # 3
    # 3
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i+1] > colh[i] + 1:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
        elif colh[i+1] > colh[i]:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
        else:
            colh[i] = highest + 3
            colh[i+1] = highest + 3
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareJ3():
    # 2 2 2
    #     2
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        if colh[i+2] >= colh[i+1] and colh[i+2] >= colh[i]:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
            colh[i+2] = highest + 2
        else:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
            colh[i+2] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareJ4():
    #   3
    #   3
    # 1 3
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        colh[i] = highest + 1
        colh[i+1] = highest + 3
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareO():
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Orot1 = compareO1()
    i = 0
    while i <= 8:
        if Orot1[i] < lowest:  # change <= or <
            lowest = Orot1[i]
            lowestIndex = i
        i = i + 1
    distribution[O1] = distribution[O1] + 1
    functions.placePiece2(lowestIndex)
    highest = getHighest2(lowestIndex)
    boardState[lowestIndex][highest+1] = 1
    boardState[lowestIndex][highest+2] = 1
    boardState[lowestIndex+1][highest+1] = 1
    boardState[lowestIndex+1][highest+2] = 1


def compareO1():
    # 2 2
    # 2 2
    # i<8, temp1-2, +{2,2}
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        colh[i] = highest + 2
        colh[i+1] = highest + 2
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareT():
    rotation = 1
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Trot1 = compareT1()
    Trot2 = compareT2()
    Trot3 = compareT3()
    Trot4 = compareT4()

    i = 0
    while i <= 7:
        if Trot1[i] <= lowest:
            lowest = Trot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 8:
        if Trot2[i] <= lowest:
            lowest = Trot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

    i = 0
    while i <= 7:
        if Trot3[i] <= lowest:
            lowest = Trot3[i]
            lowestIndex = i
            rotation = 3
        i = i + 1

    i = 0
    while i <= 8:
        if Trot4[i] <= lowest:
            lowest = Trot4[i]
            lowestIndex = i
            rotation = 4
        i = i + 1

    if rotation == 1:
        distribution[T1] = distribution[T1] + 1
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        boardState[lowestIndex][highest+1] = 1
        boardState[lowestIndex+1][highest+1] = 1
        boardState[lowestIndex+1][highest+2] = 1
        boardState[lowestIndex+2][highest+1] = 1

    if rotation == 2:
        distribution[T2] = distribution[T2] + 1
        keyPress.moveUp()
        highest = getHighest2(lowestIndex)
        functions.placePiece2(lowestIndex)
        if colh[lowestIndex+1] > colh[lowestIndex]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex+1][highest+1] = 1
        else:
            boardState[lowestIndex][highest+3] = 1
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+2] = 1

    if rotation == 3:
        distribution[T3] = distribution[T3] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        if colh[lowestIndex + 1] >= colh[lowestIndex] and colh[lowestIndex + 1] >= colh[lowestIndex+2]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+2][highest+2] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
            boardState[lowestIndex+2][highest+1] = 1

    if rotation == 4:
        distribution[T4] = distribution[T4] + 1
        keyPress.moveUp()
        keyPress.moveUp()
        keyPress.moveUp()
        highest = getHighest2(lowestIndex)
        functions.placePiece2b(lowestIndex)
        if colh[lowestIndex] > colh[lowestIndex+1]:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
        else:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+3] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1


def compareT1():
    #   2
    # 1 2 1
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        colh[i] = highest + 1
        colh[i+1] = highest + 2
        colh[i+2] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareT2():
    # 3
    # 3 1
    # 3
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i+1] > colh[i]:
            colh[i] = highest + 2
            colh[i+1] = highest + 1
        else:
            colh[i] = highest + 3
            colh[i+1] = highest + 2
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareT3():
    # 2 2 2
    #   2
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]
        if colh[i+1] >= colh[i] and colh[i+1] >= colh[i+2]:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
            colh[i+2] = highest + 2
        else:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
            colh[i+2] = highest + 1
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareT4():
    #   3
    # 2 3
    #   3
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i] > colh[i+1]:
            colh[i] = highest + 1
            colh[i+1] = highest + 2
        else:
            colh[i] = highest + 2
            colh[i+1] = highest + 3
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareS():
    rotation = 1
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Srot1 = compareS1()
    Srot2 = compareS2()

    i = 0
    while i <= 7:
        if Srot1[i] < lowest:
            lowest = Srot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 8:
        if Srot2[i] < lowest:
            lowest = Srot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

    if rotation == 1:
        distribution[S1] = distribution[S1] + 1
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        if colh[lowestIndex + 2] > colh[lowestIndex + 1] and colh[lowestIndex + 2] > colh[lowestIndex]:
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
            boardState[lowestIndex+2][highest+1] = 1
        else:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+2][highest+2] = 1

    if rotation == 2:
        distribution[S2] = distribution[S2] + 1
        keyPress.moveUp()
        highest = getHighest2(lowestIndex)
        functions.placePiece2(lowestIndex)
        if colh[lowestIndex] > colh[lowestIndex+1]:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
        else:
            boardState[lowestIndex][highest+3] = 1
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1


def compareS1():
    #   2 2
    # 1 2
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]

        if colh[i+2] > colh[i+1] and colh[i+2] > colh[i]:
            colh[i] = highest
            colh[i+1] = highest + 1
            colh[i+2] = highest + 1
        else:
            colh[i] = highest + 1
            colh[i+1] = highest + 2
            colh[i+2] = highest + 2

        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareS2():
    # 3
    # 3 2
    #   2
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i] > colh[i+1]:
            colh[i] = highest + 2
            colh[i+1] = highest + 1
        else:
            colh[i] = highest + 3
            colh[i+1] = highest + 2
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def compareZ():
    rotation = 1
    lowest = 999999
    lowestIndex = 0
    # list of all height values for L rot1
    Zrot1 = compareZ1()
    Zrot2 = compareZ2()

    i = 0
    while i <= 7:
        if Zrot1[i] < lowest:
            lowest = Zrot1[i]
            lowestIndex = i
            rotation = 1
        i = i + 1

    i = 0
    while i <= 8:
        if Zrot2[i] < lowest:  # <= to go right, < to go left
            lowest = Zrot2[i]
            lowestIndex = i
            rotation = 2
        i = i + 1

    if rotation == 1:
        distribution[Z1] = distribution[Z1] + 1
        functions.placePiece3(lowestIndex)
        highest = getHighest3(lowestIndex)
        if colh[lowestIndex] > colh[lowestIndex + 1] and colh[lowestIndex] > colh[lowestIndex + 2]:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+1][highest] = 1
            boardState[lowestIndex+2][highest] = 1
        else:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
            boardState[lowestIndex+2][highest+1] = 1

    if rotation == 2:
        distribution[Z2] = distribution[Z2] + 1
        keyPress.moveUp()
        highest = getHighest2(lowestIndex)
        functions.placePiece2(lowestIndex)
        if colh[lowestIndex+1] > colh[lowestIndex]:
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex][highest] = 1
            boardState[lowestIndex+1][highest+2] = 1
            boardState[lowestIndex+1][highest+1] = 1
        else:
            boardState[lowestIndex][highest+2] = 1
            boardState[lowestIndex][highest+1] = 1
            boardState[lowestIndex+1][highest+3] = 1
            boardState[lowestIndex+1][highest+2] = 1


def compareZ1():
    # 2 2
    #   2 1
    list = []
    i = 0
    while i <= 7:
        highest = getHighest3(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        temp3 = colh[i+2]

        if colh[i] > colh[i+1] and colh[i] > colh[i+2]:
            colh[i] = highest + 1
            colh[i+1] = highest + 1
            colh[i+2] = highest
        else:
            colh[i] = highest + 2
            colh[i+1] = highest + 2
            colh[i+2] = highest + 1

        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        colh[i+2] = temp3
        i = i + 1
        list.append(Sum)
    return list


def compareZ2():
    #   3
    # 2 3
    # 2
    list = []
    i = 0
    while i <= 8:
        highest = getHighest2(i)
        temp1 = colh[i]
        temp2 = colh[i+1]
        if colh[i+1] > colh[i]:
            colh[i] = highest + 1
            colh[i+1] = highest + 2
        else:
            colh[i] = highest + 2
            colh[i+1] = highest + 3
        Sum = sum(colh) + heightDiff(0.2)
        colh[i] = temp1
        colh[i+1] = temp2
        i = i + 1
        list.append(Sum)
    return list


def getHighest4(i):  # find highest column out of 4
    highest = 99999
    L = i
    M = L + 1
    R = M + 1
    X = R + 1
    if(colh[L] >= colh[M]):
        if(colh[L] >= colh[R]):
            highest = colh[L]
        if(colh[R] >= colh[L]):
            highest = colh[R]
    elif(colh[M] >= colh[L]):
        if(colh[M] > colh[R]):
            highest = colh[M]
        else:
            highest = colh[R]
    if(colh[X] >= highest):
        highest = colh[X]

    return highest


def getHighest3(i):  # find highest column out of 3
    highest = 99999
    L = i
    M = L + 1
    R = M + 1
    if(colh[L] >= colh[M]):
        if(colh[L] >= colh[R]):
            highest = colh[L]
        if(colh[R] >= colh[L]):
            highest = colh[R]
    elif(colh[M] >= colh[L]):
        if(colh[M] > colh[R]):
            highest = colh[M]
        else:
            highest = colh[R]
    return highest


def getHighest2(i):  # find highest column out of 2
    highest = 99999
    L = i
    R = L + 1
    if(colh[L] >= colh[R]):
        highest = colh[L]
    elif(colh[R] >= colh[L]):
        highest = colh[R]
    return highest


if __name__ == '__main__':
    main()
