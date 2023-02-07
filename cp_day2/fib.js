const findFibonacci = (num, memo = {}) => {
  if (num in memo) return memo[num]
  if (num === 0) return 0
  if (num <= 2) return 1

  memo[num] = findFibonacci(num - 1, memo) + findFibonacci(num - 2, memo)
  return memo[num]
}


console.log(findFibonacci(45))
console.log(findFibonacci(10))
console.log(findFibonacci(5))