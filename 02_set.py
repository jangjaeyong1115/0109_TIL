my_set = ['서울','서울','대전','광주','서울','대전','부산','부산']

result =[]
for i in my_set:
    if i not in result:
        result.append(i)
print(result)
print(len(result))
print(set(my_set))
print(len(set(my_set)))