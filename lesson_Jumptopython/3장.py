'''
money=True
if money:
    print("take a taxi")
else:
    print("go walk")
#띄어쓰기 간격이 서로 맞는 것이 중요. 수행문 간의 띄어쓰기 간격이 동일해야 실행된다.
'''
'''
po=['money','none']
if 'card' in po:
    print('택시를 타')
elif 'money' in po:
    print('그래도 택시를 타')
else :
    print('걸어가..')
'''
'''
hn=0
while hn<=9:
    hn=hn+1
    print('나무를 %s번 찍었습니다.'%hn)
print('나무가 쓰러졌습니다.')
#%s는 뒤의 자료형을 str으로 변환하여 받음을 복습
'''

"""
q='''
1.a
2.b
3.c
4.d'''
number=0
while number!=4:
    print(q)
    number=int(input())

if number==4:
    print('congratulate!')
else:
    pass
"""
'''
a=[(1,2),(2,3),(3,4)]
for i in a:
    A1=i[0]
    A2=i[1]
    print(A1+A2)
'''
'''
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
'''
'''for i in range(2,10):       
    for j in range(1, 10):  
        print(i*j, end='') 
    print('') 
#print는 한 번 출력하면 다음 줄로 넘어가는 함수이기에 매개변수 end를 활용해서 한 줄 내에 이어 작성하도록 한다.
'''
#3_practice
'''
i=0
a=0
while i < 1000:
    i=i+1
    if i%3==0:
        a=a+i
print(a)
'''
'''
num=1
a='*'
while num<=5:
    print(a*num)
    num=num+1
'''
'''
a=range(1,101)
for i in a:
    print(i)
'''
#range함수에 대해 숙지해둘 것
'''
A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum=0
for i in A:
    sum=sum+i
print(sum/len(A))
'''
#len함수 이름 숙지해둘 것
