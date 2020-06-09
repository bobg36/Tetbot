# this file contains all of the piece movement(left and right) functions, rotations are done in code.py
import keyPress


def placePiece4(lowestIndex):
    if lowestIndex == 0:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 1:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 2:
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 3:
        keyPress.hardDrop()

    if lowestIndex == 4:
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 5:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 6:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()


def placePiece3(lowestIndex):
    if lowestIndex == 0:
        print('index0')
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 1:
        print('index1')
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 2:
        print('index2')
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 3:
        print('index3')
        keyPress.hardDrop()

    if lowestIndex == 4:
        print('index4')
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 5:
        print('index5')
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 6:
        print('index6')
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 7:
        print('index7')
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()


def placePiece2(lowestIndex):
    if lowestIndex == 0:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 1:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 2:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 3:
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 4:
        keyPress.hardDrop()

    if lowestIndex == 5:
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 6:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 7:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 8:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()


def placePiece2b(lowestIndex):
    if lowestIndex == 0:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 1:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 2:
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 3:
        keyPress.hardDrop()

    if lowestIndex == 4:
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 5:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 6:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 7:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 8:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()


def placePiece1(lowestIndex):
    if lowestIndex == 0:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 1:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 2:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 3:
        keyPress.moveLeft()
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 4:
        keyPress.moveLeft()
        keyPress.hardDrop()

    if lowestIndex == 5:

        keyPress.hardDrop()

    if lowestIndex == 6:
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 7:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 8:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()

    if lowestIndex == 9:
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.moveRight()
        keyPress.hardDrop()
