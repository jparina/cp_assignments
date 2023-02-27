class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        curr = self.head
        statement = ""
        while curr:
            statement += f"[{curr.val}] "
            curr = curr.next
        return statement

    def add(self, val):
        new_node = Node(val)
        curr = self.tail
        if curr == None:
            self.head = new_node
            self.tail = new_node
            
        else:
            curr.next = new_node
            self.tail = new_node
            
        self.length += 1
        
    def remove(self, val):
        curr = self.head
        currplusone = curr.next
        if self.length == 0:
            print("Cannot remove from empty list")
            return
        if curr.val == val:
            self.head = currplusone
            self.length -= 1
            return curr
        while currplusone:
            if currplusone.val == val:
                curr.next = currplusone.next
                self.length -= 1
                return currplusone
            
            curr = curr.next
            currplusone = currplusone.next
        
my_linked_list = SLinkedList()
# print(my_linked_list)

my_linked_list.add(1)
my_linked_list.add(2)
# print(my_linked_list)
# print(my_linked_list.head.val, my_linked_list.tail.val)
# my_linked_list.add(2)
my_linked_list.add(3)
# my_linked_list.add(4)
# print(my_linked_list)
# my_linked_list.remove(1)
# print(my_linked_list)
my_linked_list.remove(3)
my_linked_list.remove(2)
# print(my_linked_list)
print(my_linked_list)
# print(my_linked_list.head.val, my_linked_list.tail.val)
# current = my_linked_list.head
# while current:
#     print(current.val)
#     current = current.next