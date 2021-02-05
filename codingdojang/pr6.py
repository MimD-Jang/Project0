'''
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)

예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
'''

#숫자 열 정렬
S=[1, 3, 4, 8, 13, 17, 20]
S.sort()

#차 집합 형성
n=0
subresult = []
while n < len(S)-1:
    subresult.append(S[n+1]-S[n])
    n+=1

#차집합의 최솟값 구하기
minnum = subresult[0]
for i in subresult :
    if i > minnum :
        pass
    else :
        minnum = i

'''print(minnum)'''     #중간 점검

#차집합에서 최솟값에 해당하는 순번n 구하기
n=0
count = []
for i in subresult :
    if i == minnum :
        count.append(n)
    n += 1

#원래 숫자열 쌍 구하기
for i in count :
    print(S[i],',',S[i+1])

"""
s= [1, 3, 4, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))     #zip은 본래 개수가 동일한 두 반복 가능한 자료형을 순서쌍으로 갖게 zip 객체로 변환하는 함수인데 개수가 서로 갖지 않으면 더 적은 쪽 기준으로 생성하나보다
pairs.sort(key=lambda x:x[1]-x[0])  #sorr()함수는 뒤의 key = func에 나오는 함수값에 맞게 정렬. 약식으로 x를 인수로 받아 : 뒤에 계산 값을 return하는 lambda x : x[1] - x[0] 이용하기 용이
print(pairs[0])
"""

def spair(S):
    dict = {}
    for (x, y) in zip(S[:-1], S[1:]):       #S[:-1]로 zip 순서쌍 맞춰줌
        if not dict.get(y-x):               #겹침의 유무 판별
            dict[y-x] = [(x,y)]             #list값으로 dic의 value를 설정한 건 나중에 추가하기 쉽게
        else:
            dict[y-x] = dict[y-x] + [(x,y)] #dic에 기존key가 있었다면 value list에 새로운 값 추가

    return dict[min(dict.keys())]           #min함수 쓰임 형태 확인

S = [1, 3, 4, 8, 13, 17, 20] 
#S = [1,2,4,5,8,15,19]
print(spair(S))