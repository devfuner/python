print('+------------------------------+')
print('|            야구게임           |')
print('+------------------------------+')

print('수비수 숫자')
num1 = 5;
num2 = 3;
num3 = 7;
print('숫자 > ', num1,num2,num3)

#입력받을 숫자
a = int(input('숫자를 입력하세요 > '))
print(a)
b = int(input('숫자를 입력하세요 > '))
print(b)
c = int(input('숫자를 입력하세요 > '))
print(c)

#스트라이크 & 볼
strike = 0
ball = 0

if a == b or b == c or c == a :
    print('중복된 숫자입니다.')
else:
    if num1 == a :
        strike += 1
    elif num1 == b or num2 == c:
        ball += 1
    if num2 == b:
        strike += 1
    elif num2 == a or num2 == c:
        ball += 1
    if num3 == c:
        strike += 1
    elif num3 == a or num3 == b:
        ball += 1

out = 3 - strike - ball

print('스트라이크 > ',strike)
print('볼 > ',ball)
print ('아웃 > ',out)
