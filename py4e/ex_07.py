'''fhand = open('ex_07.txt')   #굳이 open mode를 read로 쓰지 않아도 
for line in fhand:          #line에 txt file의 각 줄이 담긴다
    print(line, end='')     #txt file 의 각 줄 끝에는 \n 개행 문자가 하나씩 써져 있는 것과 마찬가지로 print()에서 end를 \n로 해줄 이유가 없다
#print(type(fhand))'''

'''fhand = open('ex_07.txt')
inp = fhand.read()
print(inp[inp.find('\n')+1:])
'''

'''fhand = open('ex_07.txt')
for line in fhand:              #그냥 fhand에서 각 반복 변수들을 하나씩 받아오면 \n을 기준으로 split돼서 받아온다.
    if line.startswith('and'):  #.startswitch() method는 결과값으로 True or False를 가져옴<- 참고로 True, False, None은 상수이며 is 연산자는 이런 상수를 다룰 때만 사용함
        line = line.rstrip()    #\n도 결국에는 whitespace의 부분집합이므로 strip() method로 삭제 가능하고 삭제한 결과물을 line에 다시 넣어줘야 한다.
        print(line)'''

#파일명을 입력 받아 파일에서 'Subject'로 시작하는 문장의 총 개수를 세는 파일
fname = input('Enter the file name:')

while True:
    try:
        fhand = open(fname)
        break
    except:
        fname = input('The file name is not correct, please enter the file name again:')

count = 0    
for line in fhand:
    if line.startswith('Subject'):
        count += 1

print('There were',count,'lines starting with "Subject" in', fname+'.')

