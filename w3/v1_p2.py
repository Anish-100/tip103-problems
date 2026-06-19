from collections import deque

def build_skyscrapers(floors):
    queue = deque(floors)
    prev = queue.popleft()
    result = 1

    while queue:
        floor = queue.popleft()
        if prev >= floor:
            prev = floor
        else:
            result +=1 
            prev = floor

    return result
        

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
