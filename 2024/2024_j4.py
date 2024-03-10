alex = input()
display = input()

silly = ""
wrong = ""
quiet = ""

org = []
dis = []

for l in display:
    if l not in alex:
        dis.append(l)
        
for m in alex:
    if m not in display:
        org.append(m)
        
org = list(set(org))
dis = list(set(dis))

# print(org)
# print(dis)

display_t = alex.replace(org[0],dis[0])   

if len(alex) - len(display) != 0:   
    display_t = display_t.replace(org[1], "")
else:
    quiet = "-"    
  
    
if display_t == display:
    silly = org[0]
    wrong = dis[0]
    if len(alex) - len(display) != 0:   
        quiet = org[1]
else:
    silly = org[1]
    wrong = dis[0]
    if len(alex) - len(display) != 0:   
        quiet = org[0]
    
print(f"{silly} {wrong}")
print(f"{quiet}")