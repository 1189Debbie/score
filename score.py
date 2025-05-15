score=input().split()
countF=0
for i in score:
  if int(i)<60:
    countF += 1
print('不及格人數:', countF)
score = list(map(int, score))
print(f'average score: {sum(score)/len(score):.2f}')
