locations = ['서울','서울','대전','부산','대전']

# 지역별 갯수를 구하삼

result = {}
for location in locations :

    if location in result:
        result[location] += 1

    else:
        result[location] = 1

print(result)