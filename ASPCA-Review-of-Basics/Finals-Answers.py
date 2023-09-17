# ANSWERS TO ASPC-A FINAL
# https://github.com/aremis9/ASPC-2023/blob/main/ASPCA-Review-of-Basics/Finals.pdf


# Problem A: AM-GM Inequality
from re import L, X


def A():
    N = int(input())
    reals = [float(i) for i in input().split()]

    sum = 0
    product = 1
    for r in reals:
        sum += r
        product *= r
    
    AM = sum / N
    GM = product ** (1/N)

    print("%.2f" % AM)
    print("%.2f" % GM)


# Problem B: A Certain Magical Index
def B():
    sentence = input()

    for x in range(len(sentence)):
        s = sentence[x]
        if s in ["a", "A"]:
            print(f"{s} found at index {x}")


# Problem C: Field of Numbers
def C():
    grid = []
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    is_sad = False

    for i in range(9):
        row = [int(i) for i in input().split()]
        if set(row) != nums:
            is_sad = True
        grid.append(row)

        if i == 3 or i == 6 or i == 8:
            if i == 8:
                i = 9

            box1 = [y for x in grid[i-3:i] for y in x[0:3]]
            if set(box1) != nums:
                is_sad = True
            
            box2 = [y for x in grid[i-3:i] for y in x[3:6]]
            if set(box2) != nums:
                is_sad = True

            box3 = [y for x in grid[i-3:i] for y in x[6:9]]
            if set(box3) != nums:
                is_sad = True

    for j in range(9):
        col = [x[j] for x in grid]
        if set(col) != nums:
            is_sad = True

    if is_sad:
        print("Sad aku.")
    else:
        print("Sudoku!")


# Problem D: Diy Latin
def D():
    word = input()

    vowels = ['a', 'e', 'i', 'o', 'u']

    if word[0] in vowels:
        print(f"{word}ay")
    else:
        print(f"{word[1:]}{word[0]}ay")
    

# Problem E: Hacking to the Gate
def E():
    N, S, K = (int(i) for i in input().split())
    D = [int(i) for i in input().split()]
    # start = S % N
    # # print(start)
    # end = (start + K) % N

    # print(D[end])

    for jumps in range(K):
        S = D[S-1]
    
    print(f"Location: {S}")


# Problem F: Cake
import math
def F():
    r = float(input())
    C = 2 * math.pi * r
    print("%.3f" % C)


# Problem G: Maximino Triples
def G():
    N = int(input())

    for i in range(N):
        scores = [int(i) for i in input().split()]
        print(f"Student {i + 1}: {max(scores)}")


# Problem H: Range Median Query
def H():
    N = int(input())
    reals = [float(i) for i in input().split()]
    Q = int(input())
    
    for i in range(Q):
        x, y = (int(i) for i in input().split())
        sub = reals[x:y + 1]
        sub.sort()
        lensub = len(sub)

        rmq = 0.0
        if lensub % 2 == 0:
            rmq = (sub[(lensub // 2) - 1] + sub[lensub // 2]) / 2
        else:
            rmq = sub[lensub // 2]

        print("%.4f" % rmq)


# Problem I: 2D Array Problem
def I():
    a, b = (int(i) for i in input().split())

    print((a * b) % 10007)


# Problem J: Drawn Onward
def J():
    N = int(input())
    test = [int(i) for i in input().split()]

    for i in range(N):
        if test[i] != test[-i - 1]:
            print("No")
            return 0
    
    print("Yes")


# Problem K: Migeee’s String Game
def K():
    s1 = input()
    s2 = input()

    M = s1.count('e')
    H = s2.count('e')

    print(M * H)


# Problem L: Hop, Step, Jump!
def L():
    s = int(input())
    
    def f(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n ==  3:
            return 4
        else:
            return f(n-1) + f(n-2) + f(n-3)

    print(f(s))


# Problem M: Dungeon Building
def M():
    N = int(input())
    room = []

    for i in range(N):
        r = [int(i) for i in input().split()]
        room.append(r)
    
    size = N * 3
    out = []
    for row in range(size):
        o = ["#" for i in range(size)]
        out.append(o)

        if (row + 1) % 3 == 0:
            i = int(((row + 1) / 3) - 1)

            for j in range(N):
                pos = (3*j) + 1
                if room[i][j] == 0:
                    out[row-1][pos] = "."
                    
                    if i > 0 and room[i-1][j] == 0:
                        out[row-2][pos] = "."
                    
                    if i < N-1 and room[i+1][j] == 0:
                        out[row][pos] = "."

                    if j < N-1 and room[i][j+1] == 0:
                        out[row-1][pos+1] = "."
                        out[row-1][pos+2] = "."

    # print(out)
    for o in out:
        print("".join(o))
    
    
M()

"""
0
1
2       (2 + 1) / 3 = 1

3
4
5       (5 + 1) / 3 = 2


"""