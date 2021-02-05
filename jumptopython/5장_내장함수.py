#all
'''for i in (0,1,2,3,4,True,False):
    if i == True :      #int자료형에서 숫자 그 자체는 1만 참이고 나머진 거짓, 리스트 자료형에서 그 값이 0이 아닌 값으로 존재한다면 참
        print('true')
    else :
        print('false')

print(all([2])) #all함수는 받는 인수가 반복 가능한 자료형인 튜플, 리스트, 딕셔너리, 문자열 등만 가능
print('\n')
print(all('is it true?')'''

#any
'''print(any([[],'',0]))
print(any([[],'',0,1]))'''

#chr -->character는 아스키(ASCII)코드 입력 받아 그 코드에 해당하는 문자 '출력'

#filter for함수가 이미 내장돼있어 각각의 요소를 받는 positive함수를 사용해야 함. 변환 값이 참인 값만 돌려주는 함수이므로 함수 결과는 참 혹은 거짓의 값을 return해야 함.
'''def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))'''

#instance
'''class Person: pass
a = Person()
print(isinstance(a, Person))'''

#map
'''def two_times(x): 
     return x*2

print(list(map(two_times, [1, 2, 3, 4])))'''

#range
'''print(range(5)) #range 자료형 자체는 튜플이나 리스트가 아닌 range자료형이라는 것
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,10,1)))
print(list(range(1,10,3)))
print(list(range(1,10,-1)))'''

#round
'''print(round(3.1))
print(round(1.23251,3))     #4째 자리에서 반올림
print(round(1.23250,3))
print(round(11276.2342,-1)) #1의 자리에서 반올림'''

#sorted
'''print(sorted((1,3,2)))  #튜플이어도 list로 값을 정렬 후 변환해주는 내장함수'''

