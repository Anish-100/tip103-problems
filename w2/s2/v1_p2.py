
# -> iterate through array and push into a dict + find the max element
# Check if there is an element of n -1 (where n is the size)
# -> for (1 to max+1)
# -> dict[i] == 1 and if i == max, then dict[max] == 2
# else return false

def is_authentic_collection(art_pieces):
    freq_dict = {}
    max_element = 0
    for element in art_pieces:
        if element in freq_dict:
            freq_dict[element]+=1
        else:
            freq_dict[element] = 13
        max_element = max(max_element, element)
    if(len(art_pieces) != max_element +1):
        return False
    for i in range(1, len(art_pieces)):
        if i not in freq_dict:
            return False
        if(i == max_element):
            if freq_dict[i] == 2:
                return True
            else:
                return False
        elif (freq_dict[i] != 1):
            return False
    return True
    

collection1 = [2, 1, 3] 
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

# [1, 2, 3, 3]
print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
