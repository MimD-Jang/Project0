'''data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))    #word_result리스트 간에 간격 ' '만큼 넣으면서 모두 str으로 join한 걸 result에 append하여 result 리스트가 생성
    print(result)
print("\n".join(result))                    #join함수는 결국 리스크간에 간격 \n을 넣고 str으로 '''

'''import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m)'''                    
#regular expression 모듈을 import해준 후 p에 re.compile을 연결해주되 매칭할 정규식을 입력해준다
#p.match()에다가 검사할 문자열을 입력해주어 그 결과 match객체를 m에다가 넣어준다.
'''m = p.match("3 python")
print(m)'''
#match는 검사할 문자열의 첫 문자부터 검사를 시작하므로 매칭이 되지 않으면 빈 값을 출력
'''m = p.search("3python")
print(m)'''
#search는 검사할 문자열 전체에서 검사를 시작해 그 결과 매칭되는 것이 있다면 match객체를 반환
'''m = p.search("3python")
print(m)'''
#위의 것과는 차이라 match객체에서 나타남. 매칭이 되는 문자열을 찾아 객체를 반환해주기는 하나 span이 1부터임이 차이
'''result = p.findall("3life is too short")
print(result)'''
#findalll함수는 특이하게도 매칭된 문자열을 리스트값으로 반환.
#띄어쓰기를 구분으로 하여 매칭하는 것이 아니기에 반환해주는 결과값은 "3life is too short"이나 "3 life is too short"이나 "life is too short" 모두 동일
'''result = p.finditer("life is too short")
print(result)'''
#이번에는 iterator 객체를 반환
'''for r in result: print(r)'''
#결과값으로는 당연히 re.match객체를 결과값으로 반환. 즉 iterator는 re.match 객체를 요소로 갖는 반복형 객체

import re
'''p = re.compile('[a-z]+')    #re.compile함수는 그 인수로 str을 받는다.
m = p.match("python")
print(m.group)              #match된 m의 문자열을 match객체형 문자열로
print(m)                    #match객체인 m을 span과 매치된 문자열로 보여준다 요즘은'''

'''p = re.compile('a.b', re.DOTALL)       
m = p.match('a\nb')
print(m)'''
#re.DOTALL은 본래 '.'가 \n을 제외한 모든 문자와 대응될 수 있는 것에서 더 나아가 모든 문자와 대응될 수 있게끔 해주는 옵션

p = re.compile('\\\\section')   
#\section이라는 문자를 받아들이고 싶으나 \s는 정규식에서 whitespace로 대응되므로 \\를 사용해 이스케이프 처리를 해줘야 한다.
#그러나 실제로 정규식에서는 \\처리를 해줘도 정규식에선 \로 해석하기 때문에 \\\\로 써줘야 정규식 해석 시 \\로 받아들여
#\\s가 이스케이프 처리되어 본래 문자인 \section으로 읽게 된다.
p = re.compile(r'\\section')
#raw string임을 표시하기 위해 r 앞에 쓰고 \\section으로 써야 한다.
#r'\string'은 whitespace처리를 할 것이고 r은 오직 \\가 사용될 때 \\를 말 그대로 \\로 사용하겠다는 뜻이므로
#r는 백슬래시가 사용되지 않을 땐 있으나 마나한 표현
