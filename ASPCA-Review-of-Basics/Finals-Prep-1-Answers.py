# ANSWERS TO ASPC-A FINALS PREPARATION 1
# https://github.com/aremis9/ASPC-2023/blob/main/ASPCA-Review-of-Basics/Finals-Prep-1.pdf


# Problem A: F91
def A():
    n = int(input())
    def f91(N):
        if N >= 101:
            return N - 10
        else:
            return f91(f91(N + 11))
    print(f91(n))


# Problem B: Do Androids Dream?
def B():
    n = int(input())
    def soul(N):
        if N == 7 or N == 9:
            print("YES")
        elif N == 5 or N <= 0:
            print("NO")
        elif N % 3 == 0:
            soul(N // 3)
        elif N % 8 == 0:
            soul(N // 8)
        else:
            soul(N - 20)

    soul(n)


# Problem C: Chocolate Box
def C():
    n = int(input())

    def fib(N):
        if N == 1:
            return 1
        elif N == 2:
            return 2
        else:
            return fib(N - 1) + fib(N - 2)
    
    print(fib(n))


# Problem D: Binary Tree
def D():
    
    def bin(L, R, x):
        if L[x] == -1 or R[x] == -1:
            return str(x)
        else:
            return str(x) + "[" + bin(L, R, L[x]) + "," + bin(L, R, R[x]) + "]"

    n = int(input())
    L = [int(i) for i in input().split()]
    R = [int(i) for i in input().split()]
    print(bin(L, R, 0))


# Problem E: Sequence Verifier
def E():
    seq = set(int(i) for i in input().split())
    if len(seq) != 7:
        return "Please debug"
    
    for s in seq:
        if s in [0, 1, 2, 3, 4, 5, 6]:
            continue
        else:
            return "Please debug"
    
    return "Sequence Valid"


# Problem F: Cipher Substitution
def F():
    plain = input()
    cyph = input()
    print(plain)
    print(cyph)

    code = {}

    for i in range(len(plain)):
        code[plain[i]] = cyph[i]
    
    for t in range(8):
        text = input()
        encoded = ""
        for c in text:
            if c in code.keys():
                encoded += code[c]
            else:
                encoded += c
        print(encoded)
