result = ['1','5','3']

# 출력결과는 153

# (1) print의 키워드(end)를 써서 출력
# (2) 반복하면서 문자열

text = ''
for element in result:
    text = text + element
print(text)

# (2 - 2) join 메서드
print(''.join(result))