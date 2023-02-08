function toRoman(int) {
  let roman = ""
  let minus = [1000,990,950,900,500,400,100,90,50,40,10,9,5,4,1]
  const numerals = {
    1 : 'I',
    4 : 'IV',
    5 : 'V',
    9 : 'IX',
    10 : 'X',
    40 : 'XL',
    50 : 'L',
    90 : 'XC',
    100 : 'C',
    400 : 'CD',
    500 : 'D',
    900 : 'CM',
    950 : 'LM',
    990 : 'XM',
    1000 : 'M'
  } 
  let i = 0
  while (int > 0) {
    if (int < minus[i]) {
      i++
      // console.log(i,int,roman)
      continue
    }
    if (int >= minus[i])
    // console.log(i,int,roman)
      int = int - minus[i]
      roman += numerals[minus[i]]
  }
  return roman
}

console.log(toRoman(4))
console.log(toRoman(9))
console.log(toRoman(14))
console.log(toRoman(44))
console.lo(toRoman(944))

