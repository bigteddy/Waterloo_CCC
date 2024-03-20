members = int(input())
rating = 0

for i in range(members):
    score = int(input())
    fouls = int(input())
    
    stars = 5 * score - 3 * fouls
    if stars > 40 :
        rating = rating + 1

if members == rating: 
    result = str(rating) + '+'
else:
    result = str(rating)
print(result)    
