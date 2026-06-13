#U: You are given the secret, actual key and the guess from the user
#.  # bulls = the digits in the correct location
#.  # cows = the digits in the number, but wrong location.
# formatting: xAyB: x = no. of bulls, y = no. of cows

# Plan: keep a freq_map of each element. 
#      Then access each element from the freq_map, if it exists, subtract 1 each time. 

## Done outside of class. 
## Final logic looked by seeing Plan part of solution, not code. 
def get_hint(secret, guess):
    secret_counts = {}
    guess_counts = {}

    bulls, cows = 0,0

    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls+=1
        else:
            if guess[i] in guess_counts:
                guess_counts[guess[i]] +=1
            else:
                guess_counts[guess[i]] = 1
            if secret[i] in secret_counts:
                secret_counts[secret[i]] +=1
            else:
                secret_counts[secret[i]] = 1
    
    for key,val in guess_counts.items():
        if key in secret_counts:
            cows+= min(guess_counts[key], secret_counts[key])
    
    return f'{bulls}A{cows}B'





secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1)) #Expected: 1A3B
print(get_hint(secret2, guess2)) #Expected: 1A1B
