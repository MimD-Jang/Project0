'''
문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

입력 예시: aaabbcccccca

출력 예시: a3b2c6a1
'''
#반복이 되지 않는다면 dic 성질을 이용해도 됐을 것 같다
s = 'aaabbcccccca'

result = []
count = 0
for x in s:
    if len(result) == 0:
        result.append(x)
        count = 1
    elif not x == result[len(result)-1]:
        result.append(count)
        result.append(x)
        count = 1
    elif x == result[len(result)-1]:
        count += 1
    
result.append(count)

#result list 안의 요소 각각을 str으로 변환해주기 map함수 사용한 후 반환 받은 list를 ''간격으로 이어 str만들기
print(''.join(map(str,result)))


s = 'aabcccaaaaas'

result = s[0]  # 첫번째 값을 결과에 넣는다
count  = 0 
for st in s:
    if st == result[-1]:  #-1은 뒤에서 첫번째 항목이므로 str 항목 수가 1개라도 index 범위를 넘지 않는다!!
        count += 1
    else:
        result += str(count) + st   #처음부터 result 반환 값을 str으로 생각해서 연산도 군더더기 없이 깔끔하다
        count = 1
result += str(count)

print(result)