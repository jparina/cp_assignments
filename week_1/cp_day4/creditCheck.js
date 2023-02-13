let credit = (num) => {
  let arr = []

  for (let i = num.length - 2; i >= 0; i-= 2) {
      let j = i + 1
      arr.push(parseInt(num[j]))
      let double = parseInt(num[i] * 2)
      if (double >= 10) {
          doubleSplit = double.toString()
          double = parseInt(doubleSplit[0]) + parseInt(doubleSplit[1])
          arr.push(double)
      } else {
      arr.push(double)
      }
  }

  let sumArr = arr.reduce((acc, current) => acc + current)

  return sumArr % 10 === 0 ? 'The number is valid!' : 'The number is invalid!'
}