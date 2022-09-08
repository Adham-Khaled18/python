import psycopg2

hostname = 'localhost'
database = 'PythonGameRecords'
username = 'postgres'
pwd = '~adhamZ18~'
port_id = 5432
conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id)
cur = conn.cursor()

board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]
currentPlayer = "X"
winner = " "
gameGoing = True
Player1 = input("Enter Player 1 name: ")
Player2 = input("Enter Player 2 name: ") 
insert_script = 'INSERT INTO gamerecords (Player1,Player2) VALUES (%s,%s)'
insert_value = (Player1,Player2)
cur.execute(insert_script,insert_value)
conn.commit()
cur.execute('SELECT id FROM gamerecords ORDER BY id DESC LIMIT 1;')
currentid = cur.fetchone()
conn.commit()
print(currentid)
def printboard(board):
    print("  |0 | 1 | 2")
    print(" ----|---|--")
    print("0 |" + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("------------")
    print("1 |" + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("------------")
    print("2 |" + board[2][0] + " | " + board[2][1] + " | " + board[2][2])


def playerInput(board):
    global currentid
    row = int(input("Enter row number: "))
    colomn = int(input("Enter colomn number: "))
    if row >= 0 and row <= 2 and colomn >=0 and colomn <=2 and board[row][colomn] == "-":
        board[row][colomn] = currentPlayer     
        insert_script = 'INSERT INTO moverecords (Symbol,row,colomn,gameid) VALUES (%s,%s,%s,%s)'
        insert_value = (currentPlayer,row,colomn,currentid)
        cur.execute(insert_script,insert_value)
        
        conn.commit()
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
insert_script = 'UPDATE gamerecords SET winner = %s WHERE id = %s'
insert_value = (winner,currentid)
cur.execute(insert_script,insert_value)
conn.commit()
cur.close()
conn.close()
