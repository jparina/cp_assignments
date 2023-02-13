# given a character or int, check if int/char in provided array
def linear_search(find, list):
    for index in range(len(list)):
        if list[index] == find:
            return index            

def global_linear_search(find, list):
    indices = []
    for index in range(len(list)):
        if find == list[index]:
            indices.append(index)
    return indices


# print(linear_search(4, [1,2,3,4]))
# print(linear_search('a', ['ad','s','d','f','g','h','j','a']))
print(global_linear_search(4, [1,2,3,4,4,1,2,4]))
print(global_linear_search('a', ['a','s','d','f','g','h','j','a']))