dic_sum = {
    "국어": 0,
    "수학": 0,
    "영어": 0,
    "도덕": 0,
    "물리": 0
}
#과목별 점수 입력
for key in dic_sum:
    score = float(input(f"{key} 점수를 입력하세요: "))
    dic_sum[key] = score

# 전체 평균 점수 계산
average = sum(dic_sum.values()) / len(dic_sum)

# 전체 평균 점수 출력
print("전체 평균 점수: ", average)
