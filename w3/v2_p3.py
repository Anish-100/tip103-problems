

def min_swap(s):
    l = 0
    r = 0
    swap = 0
    while l < r:
        if s[l] == ']' and s[r] == '[':
            s[l] = '['
            s[r] = ']'
            swap+=1
        elsif :
            l+=1
            r-=1
    return swap
        
