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

const globalLinearSearch = (find, arrayToSearch) => {
  let locations = []
  for (let i = 0; i < arrayToSearch.length; i++) {
    if (arrayToSearch[i] === find) {
       locations.push(i)
    }
  }
  return locations
}
console.log(linearSearch(1, [5,3,4,1])) // return 3
console.log(linearSearch('s', ['a','s','f', 'a'])) // return 1
console.log(globalLinearSearch('s', ['a','s','f','s'])) // return 1

