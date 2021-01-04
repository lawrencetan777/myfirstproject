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


var people = await ask("How many people live with you? (This is going to mess up if you don't put a number like 1,2,3,4 instead of one, two...) ");
parseInt(people);
if (people<2) {
console.log("Your household is too small for us");
console.log("Bye!!!!")
rl.close();
}
else if (people> 10) {
console.log("Your household is too big for us");
console.log("Bye!!!!")
rl.close();
}
else{
    console.log("Anyone is free to add questions")
}
rl.close();
}
r();