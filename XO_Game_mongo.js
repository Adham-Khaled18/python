var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb";
const ps = require("prompt-sync");
const prompt = ps();
var board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
];
var movesarr= [];
var currentPlayer = "X";
var winner = " ";
var gameGoing = true;
var Player1 = prompt("Enter Player1 name: ");
var Player2 = prompt("Enter Player2 name: ");
function drawBoard(board){
    console.log("  |0 | 1 | 2");
    console.log(" ----|---|--");
    console.log("0 |" + board[0][0] + " | " + board[0][1] + " | " + board[0][2]);
    console.log("------------");
    console.log("1 |" + board[1][0] + " | " + board[1][1] + " | " + board[1][2]);
    console.log("------------");
    console.log("2 |" + board[2][0] + " | " + board[2][1] + " | " + board[2][2]);
}
function playerInput(board){
    let row = prompt("Enter row: ");
    let colomn = prompt("Enter colomn: ");
    if (row >= 0 && row <= 2 && colomn >=0 && colomn <=2 && board[row][colomn] == "-"){
            let myobj = { "Symbol": currentPlayer , "row": row , "colomn": colomn};
            movesarr.push(myobj);
        board[row][colomn] = currentPlayer;
    }
    else{
        console.log("Invalid move! ");
        playerInput(board);
    }
}

function winCheck(board){
    if (board[0][0] == board[0][1]&& board[0][0] == board[0][2] && board[0][0]!= "-"){
        winner = board[0][0];
    }
    else if (board[1][0] == board[1][2]&& board[1][0] == board[1][1] && board[1][0]!= "-"){
        winner = board[1][0];
    }
    else if (board[2][1] == board[2][0]&& board[2][1] == board[2][2] && board[2][0]!= "-"){
        winner = board[2][1];
    }
    else if (board[0][0] == board[1][0]&& board[0][0] == board[2][0] && board[0][0]!= "-"){
        winner = board[0][0];
    }
    else if (board[0][1] == board[1][1]&& board[0][1] == board[2][1] && board[0][1]!= "-"){
        winner = board[0][1];
    }
    else if (board[0][2] == board[1][2]&& board[0][2] == board[2][2] && board[2][2]!= "-"){
        winner = board[0][2];
    }
    else if (board[0][0] == board[1][1]&& board[0][0] == board[2][2] && board[0][0]!= "-"){
        winner = board[0][0];
    }
    else if (board[0][2] == board[1][1]&& board[0][2] == board[2][0] && board[2][0]!= "-"){
        winner = board[2][0];
    }
    if (winner != " "){
        console.log("the winner is: " + winner)
        drawBoard(board)
        gameGoing = false
    }
}

function tieCheck(board){
    if (!board.some(rows => rows.includes("-"))){
        console.log("It is a tie!")
        drawBoard(board)
        gameGoing = false
    }
}
while (gameGoing){
    drawBoard(board);
    playerInput(board);
    winCheck(board);
    tieCheck(board);
    if (currentPlayer == "X"){
        currentPlayer = "O"
    }
    else{
        currentPlayer = "X"
    }
    
}
if (winner == "X"){
    winner= Player1
}
else if (winner =="O"){
    winner = Player2
}
else{
    winner = "tie"
}
MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("XOJS");
    var myobj = { "player1": Player1 , "player2": Player2 ,"winner":winner , "moves": movesarr };
      dbo.collection("GameRecords").insertOne(myobj, function(err, res) {
      if (err) throw err;
      console.log("1 document inserted");
      db.close();
    });
    
  });
