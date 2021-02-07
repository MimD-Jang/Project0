'''총 근무 시간이 40시간이 넘는다면 시간당 0.5만큼 추가 수당을 받는다는 것을 가정
만약 입력값이 숫자가 아니라면 오류 메세지 전송'''

shour = input('Enter hours : ')

i=0
while i==0:
    try:
        fhour = float(shour)
        i=1
    except:
        print('you should input number')
        shour = input('Enter hours again: ')


srate = input('Enter rate : ')

i=0
while i==0:
    try:
        frate = float(srate)
        i=1
    except:
        print('you should input number')
        srate = input('Enter rate again: ')

if fhour > 40:
    #print('overtime')
    xpay = fhour * frate + (fhour-40)*0.5
else: 
    #print('regular')
    xpay = fhour * frate
print('Pay is :',xpay)