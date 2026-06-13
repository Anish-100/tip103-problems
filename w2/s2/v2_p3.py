#U: You are given the secret, actual key and the guess from the user
#.  # bulls = the digits in the correct location
#.  # cows = the digits in the number, but wrong location.
# formatting: xAyB: x = no. of bulls, y = no. of cows

# Plan: keep a freq_map of each element. 
#      Then access each element from the freq_map, if it exists, subtract 1 each time. 

## Done outside of class. 
def get_hint(secret, guess):
    char_set = {}
    for i in secret:
        if i in char_set:
            char_set[i] +=1
        else:
            char_set[i] = 1
    correct_indexes = set()
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            correct_indexes.add(i)
            bulls+=1
            char_set[secret[i]]-=1
    for i in range(len(guess)):
        if guess[i] in char_set and i not in correct_indexes:
            if char_set[guess[i]] > 0:
                cows +=1
                char_set[guess[i]]-=1
    char_str = f'{bulls}A{cows}B'
    return char_str



secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1)) #Expected: 1A3B
print(get_hint(secret2, guess2)) #Expected: 1A1B
