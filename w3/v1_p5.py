"""
You are designing a room layout represented by a string s consisting of walls '(', ')', and decorations in the form of lowercase English letters.

Your task is to remove the minimum number of walls '(' or ')' in any positions so that the resulting room layout is balanced and return any valid layout.

Formally, a room layout is considered balanced if and only if:

It is an empty room (an empty string), contains only decorations (lowercase letters), or
It can be represented as AB (A concatenated with B), where A and B are valid layouts, or
It can be represented as (A), where A is a valid layout.

"""
def make_balanced_room(s):
    l = 0
    r = len(s) -1
    stack = []
    second_stack = []
    index_stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            index_stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0:
                second_stack.append(i)
                continue
            stack.pop()
            index_stack.pop()
    for i in index_stack:
        s = s[:i] +s[i+1:]
    for i in second_stack:
        s = s[:i] +s[i+1:]
    return s

print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 

# art(t(d)e)sign
# # Note: other outputs such as "art(t(d)esign)" would also be considered balanced and valid
# de(s)ign