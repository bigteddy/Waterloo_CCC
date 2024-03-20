p = int(input())

event_arr = [[]]
event_dict = {}
string = ''

for i in range(p):
    event = input()
    event_list = []
    for e in event:
        event_list.append(e)
    event_arr.insert(i, event_list)
    
event_arr.pop()

for j in range(5):
    count = 0
    for l in range(p):
        if event_arr[l][j] == 'Y':
            count = count + 1
    event_dict.update({j+1: count})
    
v_max = max(list(event_dict.values()))
    
# print(event_dict)
# print(max(event_dict, key = lambda x:event_dict[x]))
# print(v_max) 

for x, y in event_dict.items():
    if y == v_max:
        string = string + str(x) + ','
        
string = string[:-1]

print(string)       


        