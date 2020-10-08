import random
i = 0
restart = True
while restart:
    n = random.randint(0,100)
    print("Приветствуем в нашей игре. Попробуйте отгадать число от 1 до 100")
    restart = False
    while i < 4:
        a = int(input())
        if a == n:
            print("Поздравляю! Вы угадали")
            break
        if i == 3:
            print("Вы проиграли. Было загадано", n)
            break
        if a < n:
            print("Загаданное число больше")
        if a > n:
            print("Загаданное число меньше")
        i += 1
    if i == 3:
        i = 0
        print("Хотите начать сначала?(1 - ДА)")
        q = int( input())
        if q == 1:
            restart = True
