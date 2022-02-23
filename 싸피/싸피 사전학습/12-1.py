from typing import _SpecialForm
score=80
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

score=50
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

score=80
result="합격입니다." if score >= 60 else "불합격입니다."
print(result)

score=70
if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"
print("%d 점은 %s 등급입니다." % (score, grade)) #정수형 score 에 대한 %d 포맷 코드와 문자여려 grade에 대한 %s 포맷 코드 적용 #(score,grade) => 튜플

score=int(input("점수를 입력하세요:")) #int함수에 의해서 문자열 88이 정수 88로 변환
if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"
print("%d 점은 %s 등급입니다." % (score, grade))

