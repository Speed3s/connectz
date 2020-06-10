import sys
import fileinput

#check if connectz is playable with diamension and tokens
def notPlayable(X, Y, Z):
    return Z > X or Z > Y

#getting all the input token values and connectz format from the textfile
def getInputFileValue(list):
    for line in fileinput.input():
        list.append(line.strip())
    return list

#add token value in a grid
def placePiece(grid, inputPiece, currentPlayer):
    for grids in grid[::-1]:
        if not grids[inputPiece]:
            grids[inputPiece] = currentPlayer
            return

# check horizontal token
def checkHorizontal(grid, Z, currentPlayer):
    pieceCounter = 0
    for i in range(len(grid)):
        pieceCounter = 0
        for j in range(len(grid[i])):
            if currentPlayer == grid[i][j]:
                pieceCounter += 1
                if pieceCounter == Z:
                    return True
            else:
                pieceCounter = 0

# check vertical token
def checkVertical(grid, Z, currentPlayer):
    pieceCounter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pieceCounter = 0
            for i in range(len(grid)):
                if currentPlayer == grid[i][j]:
                    pieceCounter = pieceCounter + 1
                    if pieceCounter == Z:
                        return True
                else:
                    pieceCounter = 0

# check negative diagonal token
def checkNegDiagonal(grid, Z, currentPlayer):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pieceCounter = 0
            for k in range(Z):
                if i+k > len(grid)-1 or j+k > len(grid[i])-1:
                    break
                if currentPlayer != grid[i+k][j+k]:
                    break
                pieceCounter += 1
            if pieceCounter == Z:
                return True
    return False

# check postive diagonal token
def checkPosDiagonal(grid, Z, currentPlayer):
    pieceCounter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i < 0:
                pass
            else:
                if currentPlayer == grid[i][j]:
                    pieceCounter = pieceCounter + 1
                    i = i - 1
                    if i < 0:
                        pass
                    elif pieceCounter == Z:
                        return True
                else:
                    pieceCounter = 0
    return False

# return any winner
def checkWinner(grid, Z, currentPlayer):
    if checkHorizontal(grid, Z, currentPlayer):
        return True
    elif checkVertical(grid, Z, currentPlayer):
        return True
    elif checkNegDiagonal(grid, Z, currentPlayer):
        return True
    elif checkPosDiagonal(grid, Z, currentPlayer):
        return True

# check handling for connectz
def playConnectz():
    if len(sys.argv) != 2:
        return 'connectz.py: Provide one input file'
    else:
        try:
            ''' getting the infomation from the textfile and separate
                with dimensional frameFormat and player input token '''
            list = []
            getInputFileValue(list)
            frameFormat =  [x.split(" ") for x in list]
            X = int(frameFormat[0][0])
            Y = int(frameFormat[0][1])
            Z = int(frameFormat[0][2])
            playerInput = [int(x) for x in list[1:]]
            player = 1
            grid = [[0 for i in range(X)] for j in range(Y)]

            # Impossible game / Illegal game
            if notPlayable(X, Y, Z):
                return '7'
            for i in range(len(playerInput)):
                # Illegal column
                if 0 >= playerInput[i] or playerInput[i] > X:
                    return '6'
                # Illegal row
                elif grid[0][playerInput[i]-1] != 0:
                    return '5'
                placePiece(grid, playerInput[i]-1, player)
                # Illegal continue else Win for player 1 or player 2
                if checkWinner(grid, Z, player):
                    if len(playerInput) != i+1:
                        return '4'
                    else:
                        return player
                # DRAW
                if not any(0 in cell for cell in grid):
                    return '0'
                #change player
                player = 2 if player == 1 else 1
            # Incomplete
            return '3'
        except IOError:
            # File error
            return '9'
        except ValueError:
            # Invalid file
            return '8'


if __name__ == '__main__':
    print(playConnectz())
