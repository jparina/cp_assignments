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
  let last = null
  let grandma = "HEY KID!"
  
  while (true) {
    let response = prompt(`${grandma}`);
    if (response === "GOODBYE!" && last === true) {
      grandma = "LATER, SKATER!"
      break
    }
    else if (response === "GOODBYE!" && last !== true) {
      last = true
      grandma = "LEAVING SO SOON?"
      continue
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
    last = null
  }
  console.log(`${grandma}`)
}
deafGrandma()
// const name = prompt('HEY KID');
// console.log(`Hey there ${name}`);