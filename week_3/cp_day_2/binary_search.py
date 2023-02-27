test_array = [1,2,3,4,5]

def binary_search(num, array): 
    array.sort()
    def search(start,end):
        if start > end:
            return -1

        mid = (start+end) //2
        
        if array[mid] == num:
            return mid

        if array[mid] > num:
            return search(start, mid - 1)
        else:
            return search(mid+1, end)
    return search(0,len(array) - 1)

# print(binary_search(1, test_array) == 0)
# print(binary_search(2, test_array) == 1)
# print(binary_search(3, test_array) == 2)
# print(binary_search(4, test_array) == 3)
# print(binary_search(5, test_array) == 4)


super_big_array = [1,5,7,2,3,8,4,9]
print(binary_search(7, super_big_array) == 6)
# print(binary_search(6, super_big_array) == -1)