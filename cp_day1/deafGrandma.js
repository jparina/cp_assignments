/* 
Initial Prompt: HEY KID

If you don't input anything (just hit enter) she responds with WHAT?!

If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!

If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!

The first time you say GOODBYE! she says LEAVING SO SOON?

The second time you say GOODBYE! she says LATER, SKATER! and the program exits.

*/

function deafGrandma() {
  const prompt = require('prompt-sync')({sigint: true});
  let gooodbyeCount = 0
  let grandma = "HEY KID!"
  
  while (gooodbyeCount < 2) {
    let response = prompt(`${grandma}`);
    if (response === "GOODBYE!" && gooodbyeCount === 1) {
      gooodbyeCount += 1
      grandma = "LATER, SKATER!"
    }
    else if (response === "GOODBYE!" && gooodbyeCount === 0) {
      gooodbyeCount += 1
      grandma = "LEAVING SO SOON?"
    }
    else if (response === '') {
      grandma = "WHAT?!"
    }
    else if (response.toUpperCase() === response) {
      grandma = "NO, NOT SINCE 1946!"
    }
    else {
      grandma = "SPEAK UP, KID!"
    }
  }
  console.log(`${grandma}`)
}
deafGrandma()
// const name = prompt('HEY KID');
// console.log(`Hey there ${name}`);