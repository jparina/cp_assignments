const bottles = (numOfBottles) => {
  let currBottle = numOfBottles
  let plural = "bottles"
  let singular = "bottle"
  while (currBottle >= 0) {
    if (currBottle === 0) {
      console.log(`No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.`)
      currBottle--
    }
    else if (currBottle === 1) {
      console.log(`1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.`)
      currBottle--
    }
    else if (currBottle === 2) {
      console.log(`${currBottle} ${plural} of beer on the wall, ${currBottle} ${plural} of beer.`)
      console.log(`Take one down and pass it around, ${currBottle - 1} ${singular} of beer on the wall.`)
      currBottle--
    }
    else {
      console.log(`${currBottle} ${plural} of beer on the wall, ${currBottle} ${plural} of beer.`)
      console.log(`Take one down and pass it around, ${currBottle - 1} ${plural} of beer on the wall.`)
      currBottle--
    }
  } 
}

function noLoopBottles(numOfBottles) {
  if (numOfBottles === 0) {
    console.log(`No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.`)
  return
  }
  if (numOfBottles === 1) {
    console.log(`1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.`)
  }
  if (numOfBottles === 2) {
    console.log(`2 bottles of beer on the wall, 2 bottles of beer.`)
    console.log(`Take one down and pass it around, 1 bottle of beer on the wall.`)
  }
  if (numOfBottles > 2) {
    console.log(`${numOfBottles} bottles of beer on the wall, ${numOfBottles} bottles of beer.`)
    console.log(`Take one down and pass it around, ${numOfBottles - 1} bottles of beer on the wall.`)
  }
  noLoopBottles(numOfBottles - 1)
  return
}

noLoopBottles(4)