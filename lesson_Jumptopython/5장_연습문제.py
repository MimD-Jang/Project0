#1다음은 Calculator 클래스이다.
'''class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
#위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()   #__init__함수의 인수가 self밖에 없기 때문에 아무 인수를 안 넣어줘도 오류X
cal.add(10)
cal.minus(7)

print(cal.value)'''

#2. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 
'''class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value + val >100 :
            pass
        else:
            self.value += val

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력'''

#3. 다음 결과를 예측해 보자.
#print(all([1, 2, abs(-3)-3]))   #0이 있으니 False
#print(chr(ord('a')) == 'a')     #ord로 아키문자 a에 해당하는 값을 변환 받았다가 다시 아키 문자로 돌리니 a 나와서 True

#4. filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
'''a = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x : x>0 , a)))'''
#filter함수는 filter 타입으로 결과값을 반환하므로 보통 list가 tuple로 자료형을 변환한다.
#재사용할 함수가 아니라면 lambda함수를 활용하는 것이 현명하다
#'lambda 변수 : 함수 결과' 이 전체가 하나의 함수 문법이다.
#filter(조건 함수, 반복 가능한 자료형) 문법에서 조건 함수는 True or False 값을 반환해야 하고 그에따라 뒤의 자료형에서 filering이 이뤄진다.

#5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
"print(hex(234))"
#이번에는 int 내장 함수를 이용해 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
"print(int('0xea', 16))"  #int가 10진수이므로 이렇게 활용

#6. map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
'''print(list(map(lambda x : x*3 , [1, 2, 3, 4])))''' #filter함수와 마찬가지로 map함수도 map타입으로 결과를 반환

#7. 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
'''a = [-8, 2, 7, 5, -3, 5, 0, 1]
num = 0
maxnum = a[num]         #변수 이름을 max 함수의 이름과 동일하게 설정할 순 있지만 글자 색이 흰색이 아니면 내장함수가 존재한다는 말이니 유의할 것. 겹치면 본래의 내장 함수를 사용 못 한다.
while num < 7 :
    if maxnum > a[num+1] :
        pass
    else :
        maxnum = a[num+1]
    num = num + 1
print(maxnum)
print(max(a))'''

#8. 위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해 보자.
'''print(round(17 / 3, 4))
'''

#13. random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨).
import random
n = 0
m = 0
a = []
while n < 45 :
    a.append(random.randint(1,45))      #a에 빈 리스트를 만들었어도 길이가 0인 a list에다가 a[n] 값을 집어 넣는 건 불가능. append활용
    if n == 0 :
        pass
    else :
        for i in a:
            if i == a[n]:
                a[n] = random.randint(1,45)
    n += 1

print(a)

'''import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)     # 1부터 45까지의 난수 발생
    if num not in result:           #와우,,
        result.append(num)

print(result)'''