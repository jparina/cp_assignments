const linearSearch = (find, arrayToSearch) => {
  if (+find === find || find.toString() === find && find.length === 1) {
    return charSearch(find, arrayToSearch)
  }
  
}

function charSearch(char, array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === char) {
      return i
    }
  }
}

const globalLinearSearch = (find, arrayToSearch) => {
  let locations = []
  for (let i = 0; i < arrayToSearch.length; i++) {
    if (arrayToSearch[i] === find) {
       locations.push(i)
    }
  }
  return locations
}
// console.log(linearSearch(15, [5,3,4,1,15])) // return 4
// console.log(linearSearch('s', ['a','s','f', 'a'])) // return 1
// console.log(globalLinearSearch('z', 'asdfers')) // return 1

function math(num) {
  return multiply(num)
}

function multiply(n) {
  return n*3
}
console.log(math(5))