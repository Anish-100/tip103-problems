

def min_swap(s):
    l = 0
    r = 0
    swap = 0
    while l < r:
        if s[l] == '[' and s[r] == ']':
            l+=1
            r-=1        
        else:
            swap+=1
            s[l] = '['
            
    return swap
        
