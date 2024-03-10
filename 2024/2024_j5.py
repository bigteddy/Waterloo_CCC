import sys
sys.setrecursionlimit(100000)

hw = [[]]
ans_list = []
ans = 0

r = int(input())
s = int(input())

def write_array(a):
    wr = []
    for i in range(len(a)):
        wr.append(a[i])
    return wr

for i in range(r):
    hw.insert(i, (write_array(input())))
    
a = int(input())    
b = int(input())
    
hw.pop()

def dfs(x, y):

    if x < 0 or x >= r or y < 0 or y >= s or hw[x][y] == '*':
        return ans_list
    else:
        ans_list.append(hw[x][y])
        hw[x][y] = '*'
        dfs(x+1, y)        
        dfs(x-1, y)        
        dfs(x, y+1)        
        dfs(x, y-1)  

dfs(a, b)

for l in ans_list:
    if l == 'S':
        ans += 1
    elif l == 'M':
        ans += 5
    elif l== 'L':
        ans += 10

print(ans)
