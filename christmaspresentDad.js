const { RSA_X931_PADDING } = require("constants");
const { resolve } = require("path");
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
var player1Name;
var player1Type; // bot or human
var player2Name = "BOT OF RPS";
var numRounds = 1;
var p1wins=0;
var p2wins=0;
var draws=0;

async function start() {
    console.log("Welcome to RPS tournament!");
    player1Name = await ask("What is your name? ");
    console.log(player1Name + ". I look forward to crushing you!");

    console.log("My name is "+ player2Name);

    player1Type = await askType();

    console.log( player1Type == "bot" 
        ? "A fellow bot! Why must we fight each other?" 
        : "Humans!!!!! I eat humans for lunch!");

    numRounds = await ask("#  of rounds? ");
  
    numRounds = parseInt(numRounds);

    for(var i=1;i<=numRounds;i++){
        await playRPS(i);
    }

    console.log("SUMMARY");
    console.log("Your wins: "+ p1wins);
    console.log("My wins: "+ p2wins);
    console.log("Draws: "+ draws);

    if (p1wins>p2wins){console.log("You win the game!");}
    else if (p1wins<p2wins){console.log("You lose the game!");}
    else{console.log("Draw!");}

    rl.close();
}

async function askType() {
    var type = '';
    while (type != 'bot' && type != 'human') {
        type = await ask("Are you a human or bot? (Answer 'human' or 'bot') ");
    }
    return type;
}

async function ask(question) {
    return new Promise( (resolve)=>{
        rl.question(question, (answer)=>{
            resolve(answer);
        });
    });
}

async function playRPS(roundNum) {
    console.log("=========================");
    console.log("Round "+ roundNum + " Starts!");
    console.log("==========================");
    var p1Result;
    if (player1Type === 'human' ){
        while (p1Result != "R" && p1Result !="P" && p1Result != "S"){
            p1Result = await ask("(R)ock (P)aper or (S)cissors? ");
        }
    }
    else {
        console.log("Bot randomly chooses...");
        var r = getRandomInt(1,3);
        if(r == 1){
            p1Result = "R";
        }
        else if(r===2){p1Result = "P";}
        else if(r===3){p1Result = "S";}
    }
    console.log("You chose " + fancy(p1Result) + "! My turn...");

    var p2Result = getRandomInt(1,3);
    p2Result = p2Result == 1 ? "R" : p2Result == 2 ? "P" : "S";
    console.log("I PICKED " + fancy(p2Result));
    if (p1Result==p2Result){
        draws++;
        console.log("This is a draw");
    }
    // ALL P1 WIN SCENARIOS
    else if (
        (p1Result== "S" && p2Result == "P")
        ||(p1Result == "P" && p2Result == "R")
        ||(p1Result=="R"&&p2Result=="S")){ 
            p1wins++;
            console.log("You win");

    } else { // P2 WINS
        p2wins++;
        console.log("You lose");
    }
}

function fancy(rps){
    return rps=="R" ? "ROCK" : rps=="P" ? "PAPER" : "SCISSORS";
}

function getRandomInt(min,max) {
    var r = Math.random(); // 0-1
    return Math.floor(r * (max-min+1) + min);
}

//for (var i=0;i<30;i++) console.log(getRandomInt(1,3));

start();
