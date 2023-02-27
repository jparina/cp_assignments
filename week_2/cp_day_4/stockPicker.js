// return array of indexes

const { indexOf } = require("lodash");

var stockPicker = function(prices) {
  let minPrice = Infinity
  let maxProfit = 0
  let idxMinPrice = null
  let idxMaxPrice = null
  for (let i = 0; i < prices.length; i++) {
      if (prices[i] < minPrice) {
          minPrice = prices[i]
          
      }
      else if (prices[i] - minPrice > maxProfit) {
          maxProfit = prices[i] - minPrice
          idxMinPrice = prices.indexOf(minPrice)
          idxMaxPrice = i
      }
    }
    return [idxMinPrice, idxMaxPrice]
};

console.log(stockPicker([17,3,6,9,15,8,6,1,10]))
console.log(stockPicker([17,3,6,9,15,8,6,1,10]))
console.log(stockPicker([3,17,6,9,18,15,6,1,10]))
console.log(stockPicker([1,17,6,9,8,15,6,3,19]))
console.log(stockPicker([19,17,6,9,8,15,6,3,1]))