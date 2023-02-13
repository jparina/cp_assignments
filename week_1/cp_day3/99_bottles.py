def bottleSong ():
    currBottle = 99
    while currBottle >= 0:
        if currBottle == 0:
            print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
            currBottle -= 1
        elif currBottle == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
            currBottle -= 1
        elif currBottle == 2:
            print(f"2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
            currBottle -= 1
        else:
            print(f"{currBottle} bottles of beer on the wall, {currBottle} bottles of beer.\nTake one down and pass it around, {currBottle - 1} bottles of beer on the wall.")
            currBottle -= 1
            
bottleSong()