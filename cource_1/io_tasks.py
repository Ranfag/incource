import math

def sample():
    print("sample text")


def ex2936():
    a = int(input())
    b = int(input())
    # c - неизвестно 
    # с - корень из (b + a)
    c = math.sqrt(hypo(a, b))
    print(c)

def hypo(a , b):
    return a**2 + b**2

def ex2937():
    a = int(input())
    print(f"The next number for the number {a} is {a + 1}")
    print(f"The previous number for the number {a} is {a - 1}")  

def ex2938():
    n = int(input())
    k = int(input())
    c = k // n
    print(c)

def ex2940():
    s = 109
    v = int(input())
    t = int(input())
    if v >= 0:
        x = v * t
        print(x % s)
    else:
        x = v * t
        print((x - s) % s)
        print(s - (abs(x) % s))
