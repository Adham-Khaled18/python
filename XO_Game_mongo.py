import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["xoDB"]
gameRecords = mydb["gameRecords"]
gameMoves = mydb["gameMoves"]
board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]
currentPlayer = "X"
winner = " "
gameGoing = True
Player1 = input("Enter Player 1 name: ")
Player2 = input("Enter Player 2 name: ") 
dict = {"player1": Player1 , "player2": Player2 }
x = gameRecords.insert_one(dict)
inserted_id = x.inserted_id
def printboard(board):
    print("  |0 | 1 | 2")
    print(" ----|---|--")
    print("0 |" + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("------------")
    print("1 |" + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("------------")
    print("2 |" + board[2][0] + " | " + board[2][1] + " | " + board[2][2])


def playerInput(board):
    global inserted_id
    row = int(input("Enter row number: "))
    colomn = int(input("Enter colomn number: "))
    if row >= 0 and row <= 2 and colomn >=0 and colomn <=2 and board[row][colomn] == "-":
        dict = {"Symbol": currentPlayer , "row": row , "colomn": colomn}
        
        board[row][colomn] = currentPlayer
        add_moves_relationship(inserted_id,dict)
        
    else:
        print("Invalid move! \n")
        playerInput(board)

def winCheck(board):
    global winner , gameGoing
    if board[0][0] == board[0][1] == board[0][2] and board[0][0]!= "-":
        winner = board[0][0]
    elif board[1][0] == board[1][2] == board[1][1] and board[1][0]!= "-":
        winner = board[1][0]
    elif board[2][1] == board[2][0] == board[2][2] and board[2][0]!= "-":
        winner = board[2][1]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0]!= "-":
        winner = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1]!= "-":
        winner = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[2][2]!= "-":
        winner = board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0]!= "-":
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[2][0]!= "-":
        winner = board[2][0]
    if winner != " ":
        print("the winner is: " + winner)
        printboard(board)
        gameGoing = False
def tieCheck(board):
    global gameGoing
    if not any("-" in x  for x in board):
        print("It is a tie!")
        printboard(board)
        gameGoing = False
def add_moves_relationship(game_id,dict):
    from bson.objectid import ObjectId
    _id = ObjectId(game_id)
    dict = dict.copy()
    dict["owner_id"] = game_id
    gameMoves.insert_one(dict)

while gameGoing:
    printboard(board)
    playerInput(board)
    winCheck(board)
    tieCheck(board)
    
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    
if winner == "X":
    winner= Player1
elif winner =="O":
    winner = Player2
else:
    winner = "tie"
