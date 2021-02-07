#add로 불러들일 데이터는 이미 
#setdata로 객체변수가 다 지정된 상태이므로 객체만 불러들이면 됨
'''
class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):                  
        return self.first + self.second
a = fourcal()
a.setdata(3,7)
print(a.add())
'''

'''
class fourcal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
#a = fourcal() #__int__함수는 forucal() 클래스가 사용되면 가장 먼저 불러지는 매서드이므로 first와 second값이 미지정되어 오류
a = fourcal(3,4)
print(a.add())

#기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.
class inhfourcal(fourcal):
    variable = 100
    def sub(self):
        return self.first - self.second
    def add(self):
        return self.first + 1 #오버라이딩되어 상속 받기 전 클래스에서의 매서드를 수정
    
b = inhfourcal(7,4)
c = inhfourcal(1,2)
c.variable = 200
print(b.sub())
print(c.add())
print(inhfourcal.variable)
print(b.variable)
print(c.variable)
'''

'''
import mod1
print(mod1.add(1,2))
'''
'''
from mod1 import *  #mod1 모듈을 import한 것만으로도 mod1에 있는 함수가 사용되버리니 mod1수정
print(sub(1,2))
'''
#모듈 import 활용ver1
'''
from mod2 import *
print(PI)
a = Math(3)
print(a.solv())
'''
#ver2
'''
import mod2
print(mod2.PI)
a = mod2.Math(3)
print(a.solv())
'''
#타 디렉터리 import ver1
'''
import game.sound.echo  #import는 바로 같은 디렉터리에 있는 모듈 외의 것을 가져오려면 패키지(폴더)를 통해서 가야한다.
game.sound.echo.echo_test()
'''
#ver2
'''
from game.sound import echo
echo.echo_test()
'''
#ver3
'''
from game.sound.echo import*
echo_test()
'''
#단 import함수는 모듈 또는 패키지만 불러오는 것이 가능하다는 것은 변치 않으며
#실상 모듈의 함수를 끌어다 쓸려면 import는 최종적으로 모듈을 직접 끌고 와야한다.
#요건 불가능
'''
import game
game.sound.echo.echo_test()
'''
'''
from game.sound import *  #여기까지는 import가능.
echo.echo_test()    #__init__.py내에 __all__변수에다가 import가능한 모듈을 정의해줘야한다.
'''
#__init__.py는 해당 폴더가 패키지임을 알려주는 역할
#puthon3.3버전 이후부터는 __init__.py가 없어도 되지만 하위 버전 호환을 위해 써주는 것이 바람직

#결국 import a한 a 모듈을 기준으로 끌어다 쓴다는 a.(dot)을 사용
# from a import b로 b라는 함수를 직접 끌어다 썼으면 dot 없이 사용 가능.
#impot a.b.c로 끌어다 썼으면 함수를 사용할 때도 a.b.c.d로 사용
#main 모듈이 import하는 모든 모듈의 상위 패키지에 존재하면 하위 모듈 간의 불러오기도 성립하나 하위 모듈을 main으로 실행하면 오류.
'''from game.graphic.render import render_test
render_test()'''

#예외처리 시도 한 번 해보고 오류 발생하면 except 실행
'''try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass'''

#일부로 오류를 만드는 경우도 존재
#Eagle클래스에서 매서드 오버라이딩을 해야했는데 이를 놓칠 시에는 오류를 발송할 수 있도록
#상속받는 Bird 클래스에서 raise NotImplementedError구현하도록 설정
'''class Bird:
    def fly(self):
        raise NotImplementedError
class Eagle(Bird):
    pass
eagle = Eagle()
eagle.fly()'''

'''import pickle
data ='those are..'
f1= open('test1.txt','wb')      #bytes로 자동 변환. picle내장 함수가 뭔지는 모르지만 일반적인 읽고 쓰기도 안 되고 덤프한 걸 로드할 때도 같은 파일 객체 변수를 사용해야 한다.
pickle.dump(data,f1)
f1.close
f1 = open('test1.txt', 'rb')
data = pickle.load(f1)
print(data)
f1.close'''

'''import os
print(os.environ['PATH'])
'''

'''import shutil
shutil.copy("src.txt", "dst.txt")'''

'''import tempfile
filename = tempfile.mkstemp()
print(filename)
f = tempfile.TemporaryFile()
f.close'''

'''import time
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))'''

'''import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))'''

'''import random
print(random.randint(0,2))'''  #0,1,2 중 난수 즉, 얘는 괄호의 끝 수도 포함

'''import webbrowser
webbrowser.open("http://google.com")'''

'''import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")'''

import sys
print(sys.path)
#해당 디렉터리 주소에서 cmd. 입력하면 바로 명령 프롬프트 실행되고
#도수창에서 sys.argv에 특정 값들이 들어갔더라도 이 값은 도수창 밖으로는 저장된 값이 아니므로 코드에서 실행해도 어떤 값을 불러올 순 없다.
