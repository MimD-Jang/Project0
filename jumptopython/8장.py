#Q1 문자열 바꾸기
'''q = 'a:b:c:d'
a = q.split(':')    #split()함수는 인수를 경계로(경계값은 포함x) 각 요소를 리스트로 반환
b = '#'.join(a)     #join()변수에는 리스트값이 들어가야 한다. 앞의 문자열을 각 리스트 사이에 넣어 문자열로
print(b)'''

#Q2 딕셔너리 값 추출하기
'''a = {'A':90, 'B':80}
print(a.get('A', 60))   #딕서녀리.get()함수는 첫 번째에 호출한 key에 해당하는 value를 반환 받는 함수
print(a.get('C', 70))   #처음 호출한 key에 해당하는 key가 없으면 두 번째 매개변수로 전달된 디폴트 값을 대신 돌려준다.
'''

#Q3 리스트의 더하기와 extend 함수
'''a = [1, 2, 3]
print(id(a))
a = a + [4,5]
print(id(a))
a = [1, 2, 3]
print(id(a))
a.extend([4, 5])
print(id(a))
#리스트 더하기 실행 시 리스트a가 저장되는 주소가 변하고, extend는 저장되는 장소가 변하지 않음.'''

#Q4 리스트 총합 구하기(50 이상 요소의 총합)
'''A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
for i in A :
    if i >= 50 :
        result += i
print(result)'''

'''result = 0
while A:                # A 리스트에 값이 있는 동안
    mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄 (int형 그 자체로 뽑아냄)
    if mark >= 50:      # 50점 이상의 점수만 더함
        result += mark

print(result)           # 481 출력
'''

#Q5 피보나치 함수. 입력을 정수 n으로 받았을 때, n 이하까지의 피보나치 수열을 출력하는 함수를 작성해 보자.
'''def pibo(n) :
    result = [0, 1, 1]
    if n == 0 :
        result = [0]
    elif n == 1 :
        result = [0, 1, 1]
    else : 
        l = 3
        while result[l-1] <= n :
            a = result[l-2] + result[l-1]
            result.extend([a])
            l = len(result)
        result.pop()                        #마지막 리스트 요소 값이 n 넘으면 탈출이니 마지막 값을 빼버리는 과정
    return result
print(pibo(5))
'''

#Q6 숫자의 총합 구하기
'''#숫자를 입력하세요. 숫자 사이는 콤마로 구분하여 주세요.\n:
num = '65,45,2,3,45,8'
a = num.split(',')      #str.split(',')은 괄호 안의 str을 경계로 하여 포함하지 않고 쪼개 리스트 생성
result = 0
for i in a :
    result += int(i)    #이때 리스트의 각 요소는 str형이므로 int로 변환
print(result)
'''

#Q7 한 줄 구구단
'''n = input('구구단을 출력할 숫자를 입력하세요(2~9)\n :')
i = 1
while i < 10 :
    print(i*int(n), end=' ')    #print후에 줄 바꾸기 없애려고
    i += 1'''

#Q8 역순 저장
'''f = open('abc.txt', 'r')
a = f.readlines()
f.close()

#a.reverse()
n = len(a)
new = list(range(n))    #range()도 결과값이 immutable하므로 list로 바꿔줘야 변경 가능
count = 1
for i in a :
    i = i.strip()       #str에서 줄바꿈 문자 제거
    new[n-count] = i
    count += 1

f = open('abc.txt', 'w')
for i in new :
    f.write(i)
    f.write('\n')

f.close()'''

#Q9 평균값 구하기
'''#sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 
#평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
f = open('sample.txt','r')
a = f.readlines()
f.close
n = 0
result = 0
for i in a :
    a[n] = i.strip()
    result += int(a[n])
    n += 1

f = open('result.txt', 'w')
f.write(str(result))
print(result)'''

#Q10 사칙연산 계산기
'''class Calculator :
    def __init__(self, data) :
        self.data = data
    
    def sum(self) :
        return sum(self.data)

    def avg(self) :
        return sum(self.data)/len(self.data)
cal1 = Calculator([1,2,3,4,5])      #class()연결되자마자 인수를 대입해야하니 __init__내장 함수를 사용해야 함
print(cal1.sum())                   #class()의 sum()과 연결될 때 self 외 인수를 대입하지 않는 것으로 __init__시 self.data class 변수를 지정해야 함을 알 수 있다.
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())'''

#Q11 모듈 사용 방법
#C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 파이썬 셸을 열어 
#이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
#(즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)
'''import sys
sys.path.append("C:/Users/USER/OneDrive/'바탕 화면'/'py file'/practice")    #큰따움표 말고 작은따움표!
import mod1
print(mod1.add(1,2))        #import했어도 mod1.에서 연결해줘야만 한다.
'''

#Q12 오류와 예외 처리
'''result = 0

try:
    [1, 2, 3][3]        #index에러 발생 excpet IndexError로 이동
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3         #result = 3
finally:                #try 구문 빠져 나오기 전 finally 구문 실행
    result += 4

print(result)'''

#Q13 DashInsert 함수
#DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 
#두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
'''a = '4546793'   

def DashInsert(a) :
    data = list(map(int,a))         #map함수는 받은 iterable 자료형을 본래 저장된 메모리는 내비두고 새 자료형을 따라 만들어줌
    result = []
    n = 0
    while n < len(data)-1 :
        result.append(data[n])      #append()는 받은 항목 1개를 집어넣고 extend()는 받은 iterable 자료형의 항목을 전부 넣어준다.
        if data[n]%2 == 1 and data[n+1]%2 == 1 :
            result.append('-')
        elif data[n]%2 == 0 and data[n+1]%2 == 0 :  #elif에 & 말고 and를 쓸것
            result.append('+')
        n += 1
    result.append(data[n])

    return ''.join(map(str,result))          #list를 str으로 변환할 때는 join()으로 묶어주는데 join은 int를 전부 str으로 변환 해야 인수를 받을 수 있다.

print(DashInsert(a))'''

'''
data = "4546793"
numbers = list(map(int, data))   # 숫자 문자열을 숫자 리스트로 변경
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                   # 다음 수가 있다면
        is_odd = num % 2 == 1                # 현재 수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1  # 다음 수가 홀수
        if is_odd and is_next_odd:           # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")

print("".join(result))
'''

#Q14 연속적으로 반복되는 문자열 압축하기

'''givenstr = 'aaabbcccccca'
givenlist = list(givenstr)
def compression(listdata) :
    p = 0                                   #중복되는 횟수
    finalresult = []                        #최종 결과

    for n, i in enumerate(listdata) :       #enumerate()는 반복문 사용 시 몇 번째 반복문인지도 확인할 수 있고 이 값은 n에 담겨진다.
        if n == 0 :
            if listdata[n] == listdata[n+1] :
                p += 1
                finalresult.append(i)
            else :
                pass
        elif listdata[n-1] == listdata[n] : #a'a'이면
            p += 1

        else :                              #a'b'이면
            finalresult.append(p)
            finalresult.append(i)
            p = 1

    finalresult.append(p)

    return ''.join(map(str,finalresult))

print(compression(givenlist))'''


#리스트는 인덱스가 편리하지만 이처럼 단순 일방향으로 더해가는 알고리즘은 스트링 자료형을 계속 사용하여도 좋다.
'''
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print (compress_string("aaabbcccccca"))
'''

#Q15 Duplicate Numbers
#0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

"""q = ['0123456789', '01234', '01234567890', '6789012345', '012322456789']
result = []

#sort하면 정렬된 값이 원래 temp list 안으로 저장된다.
'''
temp = list(map(int,q[2]))
temp.sort()     
print(temp)
'''

for s in q :
    temp = list(map(int, s))
    temp.sort()
    
    if len(temp) != 10 :
        result.append('False')
    
    elif temp == [0,1,2,3,4,5,6,7,8,9] :
        result.append('True')
    
    else :
        result.append('False')

for i in result :
    print(i, end=', ')
"""
#출력값 자체가 진위 자료형임을 이용해
'''def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:       #not in 진위 구문도 자주 쓰이는 구문이니 숙지해둘 것
            result.append(num)
        else:
            return False            #else구문에 return을 배치하여 False값 자체를 내보낼 수 있다.
    return len(result) == 10        #if구문을 두번 쓸 필요 없이 바로 True값 내보내게 설정 가능
#for구문을 이용해 요약 가능
print(chkDupNum("0123456789"))      # True 리턴
print(chkDupNum("01234"))           # False 리턴
print(chkDupNum("01234567890"))     # False 리턴
print(chkDupNum("6789012345"))      # True 리턴
print(chkDupNum("012322456789"))    # False 리턴'''

#Q16 모스 부호 해독
'''
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
'''
#Q17 기초 메타 문자
'''import re

p = re.compile("a[.]{3,}b") #정규식은 기본적으로 정규표현 문자열에 맞게 콤파일 해준 것을 p에 연결해주고 []은 안의 문자와 매치됨(그냥 도트만 있있으면 \n제외한 모든 문자 가능했을 것).이때 반환값은 False가 아니라 match의 성격에 따라 None이거나 매치되는 객체를 매치 자료형으로 반환

print (p.match("acccb"))    # None
print (p.match("a....b"))   # 매치 객체 출력
print (p.match("aaab"))     # None
print (p.match("a.cccb"))   # None'''

#Q18 문자열 검색
'''import re
p = re.compile("[a-z]+")    #소문자로 이뤄진 것들만 컴파일
m = p.search("5 python")    #m에는 p.search에서 받아들인 문자열의 python가 매치
m.start() + m.end()         #첫 글자와 끝 글자 인덱스 자리수 표기.2,8'''

#