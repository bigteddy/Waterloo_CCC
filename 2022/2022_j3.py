instruction = input()
letters = ""
action = ""
turns = ""
a = ""
instruction += "?"

for char in instruction:
    if (char.isalpha() and a.isdigit()) or char == "?":
        print(f"{letters} {action} {turns}")       
        letters = ""
        action = ""
        turns = "" 
        a = ""           
    if char.isalpha():     
        letters += char
    elif char == '+':
        action = "tighten"
    elif char == '-':
        action = "loosen"
    elif char.isdigit():
        turns += char
        a = char   

# input_sequence = "AFB+8HC-4"

