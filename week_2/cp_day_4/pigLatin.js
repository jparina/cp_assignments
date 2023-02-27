const { split } = require("lodash")

function pigLatin(str) {
  let arrOfWords = str.split(' ') // ["Hi,",  "I'm", "Zach"]  ["Hi", ",", "I'm", "Zach"]  , or \n
  let outputStr = ''
  console.log(arrOfWords)
  arrOfWords.forEach(elem => {
    outputStr += translate(elem) + ' '
  })
  return outputStr
} 


function translate(str) {
  let ansStr = ''
  let splitAt = null
  let arrayOfVowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  
  for (let i = 0; i < str.length; i++) {
    if (arrayOfVowels.includes(str[i])) {
      splitAt = i
      ansStr += str.slice(splitAt) + str.slice(0,splitAt) + 'ay'
      break
    }
    
    
  }
  
  return ansStr

}

console.log(pigLatin("I go to apple university"))