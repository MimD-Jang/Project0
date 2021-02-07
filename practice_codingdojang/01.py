'''
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.

예를 들어

d(91) = 9 + 1 + 91 = 101

이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.

어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 
이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
'''
'''strdata = str(132)
a = []
for i in strdata:  #for문은 iterable한 자료형으로 str도 받는다.
    a.append(i)
print(a)'''
#1
def generator(n) :
    result = 0
    for i in str(n) :
        result += int(i)
    result += n
    return result
    
'''print(generator(100))'''

def findgenerator(n):
    generatorresult = []
    for i in range(n):
        if generator(int(i)) == n:
            generatorresult.append(i)

    if generatorresult == []:
        return n
    else:
        return generatorresult

'''print(findgenerator(3))'''

def reader(n):
    if findgenerator(n) == n:
        return n
    else:
        return 0

result = 0
for i in range(1,5001):
    result += reader(i)

print(result)

'''
#2 set()자료형을 이용해 차집합 성질 이용
print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))

#3-1 n //= 10이라는 게 조금 걸리지만 문자열로 고치고 if .. not in .. 잘 활용 
def d_fn(n):
    y = n
    while n > 0:
        y += n % 10
        n //= 10
    return y

Z = [d_fn(n) for n in range(5000)]
A = [n for n in range(5000) if n not in Z]
print (sum(A))

#3-2
def d_fn(n): return (n + sum([int(x) for x in str(n)]))

Z = [d_fn(n) for n in range(5000)]
A = [n for n in range(5000) if n not in Z]
print (sum(A))

#3-3
def d_fn(n): return (n + sum([int(x) for x in str(n)]))

S = set(range(5000))
Z = set([d_fn(n) for n in range(5000)])
print (sum(S-Z))
'''
