#시험본 과목의 갯수 N

N = int(input())
#세준이의 성적
scores = list(map(int,input().split()))
max=0
for max_score in scores: #최고점 찾기
    if max <= max_score:
        max = max_score
new_scores=[]    #최고점을 기준으로 새로운 점수로 교체
for score in scores:
    score = score/(max*100)
    new_scores.append(score)
sum=0
for new_score in new_scores:#새로운 점수로 새 평균 구하기
    sum += new_score
print(sum/len(new_scores))
