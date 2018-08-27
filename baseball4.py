import random

print('+------------------------------+')
print('|            야구게임           |')
print('+------------------------------+')

game_length = 3

print('수비수 숫자')
list=[]
num = random.randint(1, 9)

for i in range(game_length):
    while num in list:
        num = random.randint(1, 9)
    list.append(num)

# num = [5, 3, 7]
# print('숫자 > ', num)
#
guess = [num]
# input_message = ["숫자를 입력하세요 > "]

while True:
    guess.clear()
#입력받을 숫자
    for i in range(game_length) :
        guess.append(int(input("promte > ")))

    print('공격수가 고른 숫자 > ')
    for i in range(game_length):
        print(guess[i])

    if guess[0] == guess[1] or guess[1] == guess[2] or guess[2] == guess[0] :
        print("중복된 숫자입니다.")
#스트라이크 & 볼
    strike = 0
    ball = 0
    out = game_length - strike - ball

    for i in range(game_length) :
        for j in range(game_length) :
            if num[i] == guess[j]:
                if i == j :
                    strike += 1
                else:
                    ball += 1
    print('스트라이크 > ', strike)
    print('볼 > ', ball)
    print('아웃 > ', out)


    if strike == game_length :
        print('정답입니다. ')
        break