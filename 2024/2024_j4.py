alex = input()
display = input()
# silly = ""
# wrong = ""
quiet = ""
org = []
dis = []

diff = len(alex) - len(display)

for l in display:
    if l not in alex:
        dis.append(l)
        
for m in alex:
    if m not in display:
        org.append(m)
        
# print(org)
# print(dis)

org_dict = {org.count(i):i for i in org}
dis_dict = {dis.count(j):j for j in dis}

# print(org_dict)
# print(dis_dict)

if diff == 0:   
    quiet = "-"
else:
    quiet = org_dict.get(diff)
    
def find_non_key(key, dict_list):
    for k, v in dict_list.items():
        if k != key:
            return v
    
silly = find_non_key(diff, org_dict) 
wrong = find_non_key(diff, dis_dict)

print(f"{silly} {wrong}")
print(f"{quiet}")
