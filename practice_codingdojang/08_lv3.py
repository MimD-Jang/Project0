'''문제는 다음과 같다:
6 6

  0   1   2   3   4   5
 19  20  21  22  23   6
 18  31  32  33  24   7
 17  30  35  34  25   8
 16  29  28  27  26   9
 15  14  13  12  11  10
위처럼 6 6이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.'''

inp = input('please enter two numbers with whitesapce:')
#input gaurdian
while True:
    try :
        lxy = inp.split()
        x = int(lxy[0])
        y = int(lxy[1])
        break
    except:
        inp = input('please re-enter two numbers with whitesapce(ex.6 6) :')

llines = list()
for n in range(y):
    llines.append(list(range(x)))
#print(llines)

standnum = 1
inputnum = 0

for i in range(int(y/2)+1):

    #첫 반바퀴
    
    for a in range(x):
        if a < standnum-1 or a > x-standnum:
            continue
        llines[standnum-1][a] = inputnum
        inputnum += 1
    
    for b in range(y):
        if b < standnum or b > y-standnum:
            continue
        llines[b][x-standnum] = inputnum
        inputnum += 1
    
    #나머지 반바퀴
    temp = list(range(x))
    temp.sort(reverse=True)
    for a in temp:
        if x-1-standnum < a or a < standnum-1:
            continue
        llines[y-standnum][a] = inputnum
        inputnum += 1

    temp = list(range(y))
    temp.sort(reverse=True)
    for b in temp:
        if y-1-standnum < b or standnum > b :
            continue
        llines[b][standnum-1] = inputnum
        inputnum += 1

    standnum += 1

for i in llines:
    print(i)





