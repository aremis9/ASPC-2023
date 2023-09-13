# ANSWERS TO ASPC-A FINALS PREPARATION 2
# https://github.com/aremis9/ASPC-2023/blob/main/ASPCA-Review-of-Basics/Finals-Prep-2.pdf


# Problem A: Seriously, Is it Sorted?
def A():
    N = int(input())
    ints = [int(i) for i in input().split()]

    ints.sort(reverse=True)
    for i in ints:
        print(i)
    # print(ints)


# Problem B: Data Plan
def B():
    T = int(input())

    for i in range(T):
        text = input()
        print(f"Line {i + 1} is {len(text)} long.")


# Problem C: Find the Median
def C():
    N = int(input())
    reals = [float(i) for i in input().split()]
    reals.sort()

    median = 0
    if N % 2 == 0:
        median = (reals[(N//2) - 1] + reals[N//2])
    else:
        median = reals[N//2]
    
    print("%.4f" % median)


# Problem D: ASCII GUI
def D():
    texts = []
    for i in range(5):
        t = input()
        texts.append(t)
    
    print("--------------------")
    for t in range(len(texts) - 1, -1, -1):
        print(f"{t + 1}:{texts[t]}")
    
    print("--------------------")


# Problem E: Mean Ranges
def E():
    N = int(input())
    nums = [float(i) for i in input().split()]

    sum = 0
    for n in nums:
        sum += n

    range = int(max(nums) - min(nums))
    avg = sum / N
    print(range, "%.2f" % avg)


# Problem F: Dictionary Time
def F():
    N = int(input())
    words = []

    prev = ''
    result = True
    for i in range(N):
        curr = input()
        if not curr > prev:
            result = False
        prev = curr

    if result:
        print("yes")
    else:
        print("no")
    

# Problem G: Nonogram Hints
def G():
    N, M = (int(i) for i in input().split())
    line2 = [i for i in input().split()]
    cells = line2[-1]
    line2.pop()
    hints = [int(i) for i in line2]

    counts = []
    count = 0
    for c in range(N):
        if cells[c] == ".":
            if count == 0:
                continue
            else:
                counts.append(count)
                count = 0
            continue

        count += 1
        if c == N - 1 and count > 0:
            counts.append(count)

    if counts == hints:
        print("Valid!")
    else:
        print("Invalid.")


# Problem H: Top Target
def H():
    N = int(input())
    names = []
    for i in range(N):
        name = input()
        names.append(name)
    
    names_set = set(names)
    prev = ("", 0)
    ans = ("", 0)
    for name in names_set:
        freq = names.count(name)
        if freq > prev[1]:
            ans = (name, freq)
        
        prev = (name, freq)
    
    print(f"TOP TARGET: {prev[0]}")
    print(f"APPEARS {prev[1]} TIME(S)")

            
# Problem I: Panel Puzzle
# *this was not that easy
def I():
    N = int(input())

    empty = []
    sq1 = []
    for i in range(N):
        row = [i for i in input()]
        for r in range(N):
            if row[r] == '.':
                empty.append((r, i))
        sq1.append(row)
    
    colored = []
    sq2 = []
    for i in range(N):
        row = [i for i in input()]
        for r in range(N):
            if row[r] == '#':
                colored.append((r, i))
        sq2.append(row)
    
    
    def rotate90(N, coordinates):
        # 90 deg rotation:  (x,y) -> (N-y,x)
        new = []
        for ci in coordinates:
            cf = (N - ci[1], ci[0])
            new.append(cf)
        return new
    
    matchable = False
    N -= 1

    for i in range(4):
        for c in colored:
            if c not in empty:
                matchable = False
                break
            else:
                matchable = True
        if matchable:
            break
        colored = rotate90(N, colored)

    if matchable:
        print("Yes")
    else:
        print("No")







"""

     0 1 2      0 1 2

0    0 1 2      6 7 0
1    7 8 3      5 8 1
2    6 5 4      4 3 2

   y 0 1 2 3     0 1 2 3
x
0    a b c d     m i e a
1    e f g h     n j f b
2    i j k l     o k g c
3    m n o p     p l h d


90 deg:  (x,y) -> (|y-3|, )
90 deg:  (x,y) -> (y, x)

(x,y) -> (N-y,x)
(0,0) -> (3,0)
(0,1) -> (2,0)
(0,2) -> (1,0)
(0,3) -> (0,0)

(1,0) -> (3,1)
(1,1) -> (2,1)
(1,2) -> (1,1)
(1,3) -> (0,1)

(2,0) -> (3,2)
(2,1) -> (2,2)
(2,2) -> (1,2)

"""
