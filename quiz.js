const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


async function ask(question) {
    return new Promise( (resolve)=>{
        rl.question(question, (answer) => {
                resolve(answer);
            });
    });
}
async function r (){
var quizzer = await ask("What's your name? ");
 console.log("Hello, " + quizzer)

rl.close();
}
r();