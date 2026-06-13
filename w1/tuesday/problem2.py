def final_value_after_operations(operations):
    tigger = 1
    for item in operations:
        if item == 'bouncy' or item =='flouncy':
            tigger+=1
        elif item =='trouncy' or item == 'pouncy':
            tigger-=1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

