"""
You are designing a room layout represented by a string s consisting of walls '(', ')', and decorations in the form of lowercase English letters.

Your task is to remove the minimum number of walls '(' or ')' in any positions so that the resulting room layout is balanced and return any valid layout.

Formally, a room layout is considered balanced if and only if:

It is an empty room (an empty string), contains only decorations (lowercase letters), or
It can be represented as AB (A concatenated with B), where A and B are valid layouts, or
It can be represented as (A), where A is a valid layout.

"""
def make_balanced_room(s):
    second_stack = set()
    index_stack = set()

    for i in range(len(s)):
        if s[i] == '(':
            index_stack.add(i)
        elif s[i] == ')':
            if len(index_stack) == 0:
                second_stack.add(i)
                continue
            index_stack.pop()
    new_str = ""
    for i in range(len(s)):
        if i in second_stack or i in index_stack:
            continue
        else:
            new_str+=s[i]
    return new_str

print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 

# art(t(d)e)sign
# # Note: other outputs such as "art(t(d)esign)" would also be considered balanced and valid
# de(s)ign