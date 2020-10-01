a = int( input())
b = int( input())
c = int( input())
if a == 0 and b == 0 and c == 0: print("Все корни верны")
if a == 0 and b == 0: print("Уравнение не имеет смысла")
if a == 0 and c == 0: print("x = 0")
if b == 0 and c == 0: print("x = 0")
if a == 0: print("x =",-c/b)
if b == 0: print("x =",(c/a)**0.5)
if c == 0: print("x1 =0",'\n',"x2 =",-b/a)

D = b**2 - 4*a*c
if D > 0:
    print("x1 =", (-b + D**0.5)/(2*a),'\n', "x2 =", (-b - D**0.5)/(2*a))
elif D < 0:
    print("Вещественных корней не существует")
else:
    print("x =",-b/(2*a))
