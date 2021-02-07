data = "From taeho.wkdxogh3@snu.ac.kr Sat Jun  5 16:52:09 2021"
startpos = data.find('@')
# print(stpos)
# print(data[19])
stoppos = data.find(' ',startpos)
print(data[startpos+1:stoppos])

words = data.split()
emailadress = words[1]
piece = emailadress.split('@')
print(piece[1])

import re                           #import를 중간에 선언해도 무방한가보네
x = re.findall('@([^ ]*)', data)    #re.findall()함수의 결과물(list)을 x에 담을 거고 정규식 표현에 해당하는 string을 가져옴
print(x)                            #()은 여기에 있는 것들만 가져온다는 것 / []은 한 문자임을 의미 / []안의 ^ 는 공백을 제외한이라는 뜻 / *는 많은 횟수 반복 가능. 따라서 @뒤에 공백 제외한 문자열을 지칭
y = re.findall('^From .*@([^ ]*)', data)    #data의 양이 많다면 모든 줄을 앞부분만 검토해보는 게 가능하도록 효율적이게 짤 수 있다.
print(y)

'''파일에서 X-DSPAM-Confidence로 시작하고 뒤에 나온 숫자들 중 가장 큰 수를 구하는 프로그램'''

#import re
fhand = open('~.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    tof = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)    #re.findall 결과값은 탐색하는 문자열을 항목으로 갖는 리스트형 자료
    if len(tof) != 1: continue
    num = float(tof[0])
    numlist.append(num)
print('Maximum is:',max(numlist))
