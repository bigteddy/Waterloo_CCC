
code = []

while True:
    info = input()
    if info == '99999':
        break
    else:
        code.append(info)
    
# print(code)

for i in code:
    if (int(i[0]) + int(i[1])) == 0:
        pass
    elif (int(i[0]) + int(i[1])) % 2 == 0:
        dir = 'right'
    else:
        dir = 'left'
    
    step = int(i[2] + i[3] + i[4])        
    print(f"{dir} {step}")
   

