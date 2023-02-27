# Create a linked list that only supports adding or removing from the end
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self):
        if self.head == None:
            return None
        current = self.head
        self.head = current.next
        self.length -= 1
        return current


# stack = LinkedListStack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# x = stack.pop()
# print(stack.length)
# print(x.val)

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def enqueue(self, val):
        new_node = Node(val)
        new_node.next = None
        if not self.head:
            self.head = new_node
        if self.tail:
           self.tail.next = new_node 
        self.tail = new_node
        self.length += 1
        
    def dequeue(self):
        if not self.head:
            return "Empty List"
        curr = self.head
        self.head = curr.next
        return curr

# bam = LinkedListQueue()
# # print(bam.length)
# bam.enqueue(10)
# print(bam.length)
# print(bam.head.val)
# print(bam.tail.val)
# print("-------------")
# bam.enqueue(20)
# print(bam.length)
# print(bam.head.val)
# print(bam.tail.val)
# print(bam.dequeue().val)
# print(bam.head.val)
class DblNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        # Show the linked list i.e. head: 5 --> 6 --> 7 --> None
        if self.length == 0:
            return "Empty List"
        display_str = "Head: "
        current = self.head
        while current:
            display_str += f"{current.val} --> "
            current = current.next

        display_str += "None"
        return display_str
        
    def push(self, val):
        new_node = DblNode(val)
        if self.tail:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        
        last_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = last_node.prev
            current.next = None
            self.tail = current
        
        self.length -= 1
        return last_node
    
    def insert(self, val, insert_at_index):
        if insert_at_index == self.length:
            self.push(val)
            
        elif insert_at_index > self.length:
            return "Index Error: List out of range"
        
        else:
            new_node = DblNode(val)
            current = self.head
            current_index = 0
            
            while current_index < insert_at_index:
                current = current.next
                current_index += 1
            
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node
            self.length += 1
            
    
    def remove(self, remove_at_index):
        if remove_at_index >= self.length:
            return "Index Error: Out of range"
        
        if remove_at_index == 0:
            node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None 
            self.length -= 1
            return node
            
        if remove_at_index == self.length - 1:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return node
        
        else:
            current = self.head
            current_index = 0
            while current_index < remove_at_index:
                current = current.next
                current_index += 1

            node = current
            previous = current.prev
            previous.next = current.next
            current = current.next
            current.prev = previous
            self.length -= 1
            return node
    
    def iterative_search(self, val):
        # Step through LL to find val or return None
        pass
    
    def recursive_search(self, val):
        pass
    
    
sample_list = DoublyLinkedList()
print(sample_list)

sample_list.push(10)
print(sample_list)

sample_list.push(15)
print(sample_list)

sample_list.remove(0)
print(sample_list)