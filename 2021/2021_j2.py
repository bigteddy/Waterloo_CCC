num = int(input())
bid = {}

z = 0
for i in range(num):
    x = input()
    y = int(input())
    z = bid.get(x)
    if z is not None:
        if y < z:
            y = z
            z = 0
    bid.update({x: y})
    
# print(bid)
key = ''
val = 0
for x, y in bid.items():
    if y > val:
        key = x
        val = y

# print(bid)
print(key)