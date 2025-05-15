
score = list(map(int, score))
max=score[0]
min=score[0]
countF=0
for i in score:
  if int(i)<60:
    countF += 1

print('不及格人數:', countF)
print(f'average score: {sum(score)/len(score):.2f}')
