function isAnagram(str1, str2) {
  let newStr1 = str1.toUpperCase()
  let newStr2 = str2.toUpperCase()
  let charsCount = {}
  let charsCount2 = {}

  for (let letter of newStr1) {
    if (letter === ' ') {
      continue
    }
    if (charsCount[letter]) {
      charsCount[letter] += 1
    }
    else {
      charsCount[letter] = 1
    }
  }
  
  for (let letter of newStr2) {
    if (letter === ' ') {
      continue
    }
    if (charsCount2[letter]) {
      charsCount2[letter] += 1
    }
    else {
      charsCount2[letter] = 1
    }
  }
  for (let key in charsCount) {
    if (charsCount[key] !== charsCount2[key]) {
      return false
    }
  }

  return true
}

// console.log(isAnagram('asd', 'dsa'))

// console.log(isAnagram('charm', 'march'))
// console.log(isAnagram('CharM', 'mARcH'))
// console.log(isAnagram('Anna Madrigal', 'A man and a girl'))


function anagrams_for(str1, array) {
  let newStr1 = str1.toUpperCase()
  let charsCount = {}
  let listOfAnagrams = []
  for (let letter of newStr1) {
    if (letter === ' ') {
      continue
    }
    if (charsCount[letter]) {
      charsCount[letter] += 1
    }
    else {
      charsCount[letter] = 1
    }
  }

  for (let word of array) {
    word2 = word.toUpperCase()
    charsCount2 = {}
    anagram = true
    for (let letter of word2) {
      if (letter === ' ') {
        continue
      }
      if (charsCount2[letter]) {
        charsCount2[letter] += 1
      }
      else {
        charsCount2[letter] = 1
      }
    }
    for (let key in charsCount2) {
      
      if (charsCount[key] !== charsCount2[key]) {
        anagram = false
        break
      }
    }
    if (anagram === true) {
      listOfAnagrams.push(word)
    }
  }
  return listOfAnagrams
}

listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

console.log(anagrams_for('threads', listOfWords))