#5
'''a="a:b:c:d"
b=a[:3]
print(b)
c=a.replace(":","#")
print(c)
print(a)
print("힘드네")
'''
#6
'''a=[1,3,5,4,2]
a.sort()
b=a
print(b)
b.reverse()
print(b)
#reverse함수는 replace와는 다르게 변환된 값이 기존 객체에 그대로 남아있다.
'''
#7
'''a=['life', 'is', 'so','short']
b=" ".join(a)
print(b)
#join은 앞의 객체를 목적어가 되는 a객체 사이사이에다가 합친다.
'''
#8
'''
a=1,2,3
b=4,
c=a+b
print(c)
#8-1
a1=1,2,3
a1=2,3,4
print(a1)
#8-1에서 볼 수 있듯 튜플은 본래 부동 객체이기에 a1은 그저 새로 생성된 튜플을 새로이 가리키는 것일 뿐 튜플 자체를 바꾼 건 아니다.
'''
#10
'''
a={'A':90, 'B':80, 'C':70}
answer=a['B']
print(answer)
#9-1
result=a.pop('B')
print(result)
print(a)
'''
#11
'''
a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b=set(a)
result=list(b)
print(result)
'''
#12
'''a = b = [1, 2, 3]
a[1] = 4
print(b)
#a와 b가 같은 리스트 객체를 가리키고 있으므로 a가 가리키는 리스트가 바뀌면 결국 b가 가리키는 리스트가 바뀌는 것과 같은 결과
#12-1
a2=[1,2,3]
b2=[1,2,3]
a2[1]=4
print(b2)
#따라서 a2와 b2는 같아 보이는 리스트여도 서로 다르게 할당된 리스트를 가리키고 있어 위와는 별개의 결과 산출
'''
