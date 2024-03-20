num = int(input())
# pepper_added = []
spiciness = 0
pepper_dict = {"Poblano":1500, "Mirasol":6000, "Serrano":15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}


for i in range(num):
    # pepper_added.append(input())
    pepper = input()
    spiciness += pepper_dict.get(pepper)
    
print(spiciness)
