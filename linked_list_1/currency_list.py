class Denomination:
    def __init__(self, val = None, count = 0, single = 'bill', plural = 'bills', cent = False, next = None):
        self.val = val
        self.count = count
        self.single = single
        self.plural = plural
        self.cent = cent
        self.next = next
   
class CurrencyLinkedList:
    def __init__(self):
        self.head = None
        
bills = CurrencyLinkedList()
coins = CurrencyLinkedList()

penny = Denomination(val=1, single='penny', plural='pennies',cent=True)

nickel = Denomination(val=5, single='nickel', plural='nickels',cent=True, next=penny)

dime = Denomination(val=10, single='dime', plural='dimes',cent=True, next=nickel)

quarter = Denomination(val=25, single='quarter', plural='quarters',cent=True, next=dime)

one = Denomination(val=1)

five = Denomination(val=5, next=one)

ten = Denomination(val=10,next=five)

twenty = Denomination(val=20, next = ten)

fifty = Denomination(val=50,next=twenty)

hundred = Denomination(val=100,next=fifty)

bills.head = hundred

coins.head = quarter




