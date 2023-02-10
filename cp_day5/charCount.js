function mergeSort(array) {
  // console.log('merge sort running')
  if (array.length <= 1) {
    console.log(array)
    return array
  }
  else {
    let midpoint = Math.floor(array.length / 2)
    let leftHalf = array.slice(0,midpoint)
    let rightHalf = array.slice(midpoint)
    return merge(mergeSort(leftHalf), mergeSort(rightHalf))
  }

  
  function merge(leftArray, rightArray) {
    
    // this function takes in two arrays and returns a single array
    // that single array is in increasing order
    leftArray.push(Infinity)
    rightArray.push(Infinity)
    
    let merged = []
    let indexLeft = 0
    let indexRight = 0

    while (leftArray[indexLeft] !== rightArray[indexRight]) {
      if (leftArray[indexLeft] < rightArray[indexRight]) {
        merged.push(leftArray[indexLeft])
        indexLeft++
      }
      if (rightArray[indexRight] < leftArray[indexLeft]) {
        merged.push(rightArray[indexRight])
        indexRight++
      }
    }
    // console.log(merged)
    return merged
  }  
}


const charCount = (toCount) => {
  const charHash = {}
  
  const ans = []
  for (let char of toCount) {
    if (char === ' ') {
      continue
    }
    if (!charHash[char]) {
      charHash[char] = 1
    }
    else {
      charHash[char] += 1
    }
  }
  let counts = Object.values(charHash)
  // console.log(counts)
  const sortedCounts = mergeSort(counts)
  return sortedCounts
  // console.log(sortedCounts)
}

console.log(charCount("an apple a day will keep the doctor away"))
// console.log(mergeSort([3,2,5,7,1,4,9,6,8]))