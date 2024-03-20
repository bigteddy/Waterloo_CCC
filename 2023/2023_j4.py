col = int(input())

Triangle = [[]]
sum = 0

a = input().split()
a.append('0')
Triangle.insert(0,a)

b = input().split()
b.append('0')
Triangle.insert(1,b)

Triangle.pop()

# def print_arr(hwr):
#     for row in hwr:
#         print(row)
        
# print_arr(Triangle)

for i in range(len(a)):
    if Triangle[0][i] == '1':
        sum = sum + 3
        if Triangle[0][i+1] == '1':
            sum = sum - 2

for i in range(len(b)):
    if Triangle[1][i] == '1':
        sum = sum + 3
        if Triangle[1][i+1] == '1':
            sum = sum - 2
        if Triangle[0][i] == '1' and i%2 == 0:
            sum = sum - 2

print(sum)