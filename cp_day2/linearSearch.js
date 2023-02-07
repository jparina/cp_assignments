const linearSearch = (find, arrayToSearch) => {
  if (find.toString().length === 1) {
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

console.log(linearSearch(1, [5,3,4,1])) // return 3
console.log(linearSearch('s', ['a','s','f'])) // return 1