score = []
third_score = 0
third_num = 1

for num in range(int(input())):
    score.append(int(input()))
    
  
score = [v for v in score if v != max(score)]
score = [v for v in score if v != max(score)]


third_score = max(score)
third_num = score.count(max(score))

print(f"{third_score} {third_num}")  
