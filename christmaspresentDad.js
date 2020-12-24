const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

var player1Name;

rl.prompt("player1 name?");

rl.on("line", (answer) => {
    console.log("Hi player 1, your name is " + answer);
    player1Name = answer;
    rl.close();
    }
);
