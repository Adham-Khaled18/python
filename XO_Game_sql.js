const ps = require("prompt-sync");
const prompt = ps();
var board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
];
var currentPlayer = "X";
var winner = " ";
var gameGoing = true;

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
        board[row][colomn] = currentPlayer;
    }
    else{
        console.log("Invalid move! ");
        playerInput(board);
    }
}

function winCheck(board){
    if (board[0][0] == board[0][1] == board[0][2] && board[0][0]!= "-"){
        winner = board[0][0]}
    else if (board[1][0] == board[1][2] == board[1][1] && board[1][0]!= "-"){
        winner = board[1][0]}
    else if (board[2][1] == board[2][0] == board[2][2] && board[2][0]!= "-"){
        winner = board[2][1]}
    else if (board[0][0] == board[1][0] == board[2][0] && board[0][0]!= "-"){
        winner = board[0][0]}
    else if (board[0][1] == board[1][1] == board[2][1] && board[0][1]!= "-"){
        winner = board[0][1]}
    else if (board[0][2] == board[1][2] == board[2][2] && board[2][2]!= "-"){
        winner = board[0][2]}
    else if (board[0][0] == board[1][1] == board[2][2] && board[0][0]!= "-"){
        winner = board[0][0]}
    else if (board[0][2] == board[1][1] == board[2][0] && board[2][0]!= "-"){
        winner = board[2][0]}
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
