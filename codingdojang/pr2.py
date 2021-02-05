'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
print(sum([x for x in range(1,1000) if x%3 == 0 or x%5 == 0]))  #for구문이 실제에서 가장 바깥에 감싸주는 구문이지만, if가 더 뒤에 위치한다~

#set함수 응용하는 법도 아주 좋음
'''
set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))

print sum(set3 | set5)          #set3과 set5의 합집합
'''