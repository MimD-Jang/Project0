#Q1.주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
'''
def is_odd(a):
    if a%2==0:
        print("주어진 자연수는 짝수입니다.")
    else:
        print("주어진 자연수는 홀수입니다.")
a=int(input("자연수를 기입해주세요.\n"))
is_odd(a)
'''
#Q2.입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
#※ 평균 값을 구할 때 len 함수를 사용해 보자.
'''
nums=list(input("input numbers.\n"))
while ',' in nums :
    nums.remove(',')    #pop()함수는 인수가 int라서 n번째 항을 내보내는 기능
print(nums)
def avg(a):
    rs1=0
    for i in a:
        rs1=rs1+int(i)  #a는 기본 list로 파악되고 거기서 for함수는 i를 str으로 뽑으니 int로 변환
    rs2=rs1/len(a)
    return rs2
print(avg(nums))
'''
#input으로 받는 게 아니라 직접 입력 받을 시
'''
def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
     result = 0
     for i in args:
         result += i
     return result / len(args)
print(avg_numbers(1,2,3))
'''
#Q3.
'''
다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
이 프로그램을 수행해 보자.

첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

※ int 함수를 사용해 보자.
'''
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))    #역시나 input 결과값은 str으로 저장된다는 점

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
'''
#Q4
'''
print("you" "need" "python")
youneedpython
>>> print("you"+"need"+"python")
youneedpython
>>> print("you", "need", "python")   # 콤마가 있는 경우 공백이 삽입되어 더해진다.
you need python
>>> print("".join(["you", "need", "python"]))
youneedpython
'''
#Q5
'''
다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 
다시 그 파일을 읽어서 출력하는 프로그램이다.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f2 = open("test.txt", 'r')
print(f2.read())
이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 
우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
'''
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()                      #f1.close가 아니라 f1.close()라는 점!
f2 = open("test.txt", 'r')
print(f2.read())
'''
#Q6.사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
#(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
'''
input = input("write anything you want.\n=>")
f = open("test.txt",'a')
f.write('\n'+input)
'''
#Q7.다음과 같은 내용을 지닌 파일 test.txt가 있다.
'''Life is too short
you need java'''
#이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.※ replace 함수를 사용해 보자.
'''
f=open('test.txt','r')
a=f.read()      #readlines는 리스트로, read는 str으로, replace()는 str만 취급
f.close()
b = a.replace('java','python')
f2 = open('test.txt', 'w')
f2.write(b)
f2.close()
'''

