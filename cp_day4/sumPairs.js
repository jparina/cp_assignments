let sumPairs = (arr, input) => {
  let ansList = []

  for (let num of arr) {
     
      for (let num2 of arr) {
          let sum = 0
          if (num2 !== num) {
              sum = num + num2
              if (sum === input) {
                  arr.splice(arr.indexOf(num2))
                  ansList.push([num,num2])
              }
          }
      }
  }

  return ansList.length === 0 ? "unable to find pairs" : ansList
}

console.log(sumPairs([1,2,3,4,5], 9)) // => [[4,5]]
console.log(sumPairs([1,2,3,4,5], 7)) // => [[2,5], [3,4]]
console.log(sumPairs([1,2,3,4,5], 27)) // => 'unable to find pairs'