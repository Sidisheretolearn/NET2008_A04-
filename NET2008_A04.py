#Sidhant Kumar 


#Example of input --> ----K---    or -----B--


print("CHESS SCORE KEEPING")
print()
instructions = input("Would you like some instructions? ===>")
if(instructions =="Yes" or "yes" or "Yes"):
    print("You have to input the white or black chess pieces.(ex, ---K----) You can only put 8 characters in the input or else in will fail. After you finish the game, you can decide to quit or continue to remove or rearrange the pieces. ")
    print()
    print("Lets begin!!!!")
elif (instructions == "q"):
    print("Thanks")
else:
    print("Lets begin!!!!")
#This function will verify if the input is valid
def VerifyRow(list):
 #These are the black(uppercase) and white(lowercase) pieces
    pieces = ["K","k","Q","q","B","b","N","n","R","r","P","p","-"]   
#List has 8 string values   
    if(len(list) != 8):               
        return False
    for i in range(len(list)):
        if(list[i] not in pieces):
            return False
    return True



#This function takes the string and adds it to the list
def convertToList(stringInput):
    list = []

    for i in range(len(stringInput)):
        list.append(stringInput[i])
    return list

#This function prints the board on the terminal 
def printBoard(board):
    for i in range(len(board)):
        print(board[i])



#This funtion gives the userinput
def userInput():
    chessList = []

    for i in range(8):
        Input = input("Enter row " + str(i) +" of chess ==>  ")
        TempList = convertToList(Input)
        print("TempList is ", TempList)
        
        while True:
            if(VerifyRow(TempList) == True):
                print("Row is Valid")
                break
            else:
                print("Invalid Row ")
                Input = input("Enter row of chess:  ")
                TempList = convertToList(Input)
        chessList.append(TempList)
    printBoard(chessList)
    return chessList
        


#This funciton founds what score to give
def DetermineScore(board):

    whiteScore = 0.0
    blackScore = 0.0

    for i in range(len(board)):
        for j in range(len(board[i])):
            Pos = board[i][j]

            if("K" == Pos):
                blackScore+= 0.0
            elif("k" == Pos):
                whiteScore+=0.0
    
            elif("Q" == Pos):
                blackScore +=10.0
            elif("q" == Pos):
                whiteScore += 10.0
    
            elif("B" == Pos):
                blackScore +=3
            elif("b" == Pos):
                whiteScore+=3
    
            elif("N" == Pos):
                blackScore+=3.5
            elif("n" == Pos):
                whiteScore+=3.5
    
            elif("R" == Pos):
                blackScore+=5.0
            elif("r" == Pos):
                whiteScore+=5.0
            
            elif("P" == Pos):
                blackScore+=1.0
            elif("p" == Pos):
                whiteScore+=1.0
#prints out score
    print("White Score is ", str(whiteScore))
    print("Black Score is ", str(blackScore))
#This determines which team wins (W vs B)
    if(whiteScore > blackScore):
        return "White",board
    elif(blackScore > whiteScore):
        return "Black",board
    return "None",board


#This function has option to continue or quit
def main():
    repos = False
    while True:

        #ask for userInput()2
        if(repos == False):
            chessBoard = userInput() 
        else:
            reposCoorX = int(input("What X position would you like to reposition ==> "))      #Enter a number for x and y value
            reposCoorY = int(input("What Y position would you like to reposition ==> "))
            reposPlay  = input("What piece would you want there ==> ")
            
            if(reposCoorX >= 0 and reposCoorX <= 8):
                if(reposCoorY >= 0 and reposCoorY <= 8):
                    chessBoard[reposCoorX][reposCoorY] = reposPlay

        Winner,board = DetermineScore(chessBoard)

        print("Winner is " + str(Winner))

        choice = input("Quit(q) or try another chessboard(a) or reposition current board(r) : ")
        if(choice == "q"):
            break
        elif(choice == "r"):
            repos = True
        elif(choice == "a"):
            repos = False

    print("Bye!")

main()
