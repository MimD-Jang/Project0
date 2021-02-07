'''1~1000에서 각 숫자의 개수 구하기'''

'''a = {1 : 2, 3 : 4}
a[2] = 4
print(list(a.keys()))'''

result = {}

for x in range(1,1001) :
    for a in str(x) :
        if a in list(result.keys()) :
            result[a] += 1
        else :
            result[a] = 1
print(result)

# 딕셔너리에 키를 설정할 때도 for문을 이용해서 설정 가능. 
'''
count={ x:0 for x in range(0,10) }

for x in range(1,1001):
    for i in str(x):
        count[int(i)]+=1

print(count)
'''