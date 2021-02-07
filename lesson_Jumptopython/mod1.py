def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(__name__)
if __name__ == "__main__" : 
    print("이게 과연 출력될까")
#__name__변수는 특별한 내장 변수. 이 파일에서 직접 이 모듈을 실행하면
#__name__에 "__main__"이 저장되고
#타 파일에서 이 모듈을 끌어서 사용하면 __name__에는 "mod1"이 저장된다.