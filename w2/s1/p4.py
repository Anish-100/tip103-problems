# frequency of every letter present in the code is equal
# must remove exactly one letter from the message

# Create a dict, letter -> counts
# Iterate through that dict, and freq = all
#  2 vars: max_freq, max_key

def can_make_balanced(code):
    freq_dict = {}
    max_freq = 0
    max_key = 0
    n_value = 0 

    for c in code:
        if c in freq_dict:
            freq_dict[c]+=1
        else:
            freq_dict[c]=0
        if (freq_dict[c] > max_freq):
            max_key = c
        max_freq = max(freq_dict[c],max_freq)
    freq_dict[max_key]-=1
    n_value = freq_dict[max_key]

    for _,val in freq_dict.items():
        if(val != n_value ):
            return False
    return True

code1 = "aarrghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 

#True
#False