print('+------------------------------+')
print('|            야구게임           |')
print('+------------------------------+')

print('수비수 숫자')
num = [5, 3, 7]
print('숫자 > ', num)

#입력받을 숫자
guess = []
print('입력받을 숫자 > ')
guess.append(int(input()))
print('입력받을 숫자 > ')
guess.append(int(input()))
print('입력받을 숫자 > ')
guess.append(int(input()))

#스트라이크 & 볼
strike = 0
ball = 0

if guess[0] == guess[1] or guess[1] == guess[2] or guess[2] == guess[0] :
    print('중복된 숫자입니다.')
else:
    if num[0] == guess[0] :
        strike += 1
    elif num[0] == guess[1] or num[0] == guess[3]:
        ball += 1
    if num[1] == guess[1] :
        strike += 1
    elif num[1] == guess[0] or num[1] == guess[0]:
        ball += 1
    if num[2] == guess[2] :
        strike += 1
    elif num[2] == guess[0] or num[2] == guess[1]:
        ball += 1

#아웃 체크
out = 3 - strike - ball

print('스트라이크 > ',strike)
print('볼 > ',ball)
print ('아웃 > ',out)