class ContactList:
    def __init__(self, name, list_of_friends) -> None:
        self.name = name
        self.list_of_friends = list_of_friends
    
    def add_contact(self, contact):
        for person in contact:
            self.list_of_friends.append(person)
        self.list_of_friends = sorted(self.list_of_friends, key=lambda dict: dict['name'])
        
    def remove_contact(self, name_to_remove):
        for i in range(len(self.list_of_friends)):
            # print(self.list_of_friends[i]['name'])
            if self.list_of_friends[i]['name'] == name_to_remove:
                self.list_of_friends.pop(i)
                break
        
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}] 
my_friends_list = ContactList('My Friends', friends)


my_friends_list.add_contact([{'name':'Anna', 'number':'555-5555'}, {'name':'Bill', 'number' : '123-456'}])

# print(my_friends_list.list_of_friends)
# my_friends_list.remove_contact('Bob')
# print(my_friends_list.list_of_friends)

