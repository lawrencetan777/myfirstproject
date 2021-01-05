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
 console.log ("**RULES**")
 console.log ("Answer the questions! (obviously)")
 console.log ("For number questions, answer with a number, not word form (e.g. 1, not one)")


var people = await ask("How many people live with you?  ");
parseInt(people);
if (people<2) {
console.log("Your household is too small for us");
console.log("Bye!!!")
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

var age = await ask("How old are you? ")
if (age<9) {
    console.log ("You're too young!");
    console.log("Bye!!!!")
rl.close();
}
if (age>50) {
    console.log ("You're too old!");
    console.log("Bye!!!!")
rl.close();
}
var color =await ask("What is your favorite color ");
console.log(color+" is your favorite color");
rl.close();
}
r();