# ANSWERS TO ASPC-A MIDTERM CONTEST
# https://github.com/aremis9/ASPC-2023/blob/main/ASPCA-Review-of-Basics/Midterm.pdf


# Problem A: Range Sum Query
def A():
    N = int(input())
    list = [int(x) for x in input().split()]
    a, b = (int(x) for x in input().split())

    sum = 0
    for i in range(a, b + 1):
        sum += list[i]

    print(f"RQS({a},{b})={sum}")

# Problem B: Countdown
def B():
    a, b = (int(x) for x in input().split())

    for i in range(b, a - 1, -1):
        print(i)

# Problem C: Cancellable Quiz
def C():
    N = int(input())
    scores = [int(s) for s in input().split()]
    scores.sort()

    sum = 0
    for s in scores:
        sum += s

    print(f"Raw Score={sum}/{10*N}")
    print(f"Final Score={sum-scores[0]}/{10*(N-1)}")

# Problem D: Printing Diamonds
def D():
    T = int(input())
    # Ns = []
    for i in range(T):
        # Ns.append(int(input())) 

    # print("-------")
    # for N in Ns:
        
        N = int(input())
        for i in range(N):
            print(" " * (N - i - 1), end = "")
            print("*" * ((2 * i) + 1))
        for j in range(N - 1, 0, -1):
            print(" " * (N - j), end = "")
            print("*" * ((2 * j) - 1))

# Problem E: User Accounts
def E():
    a, b = (int(x) for x in input().split())

    for x in range(a, b + 1):
        if x < 10:
            print(f"team0{x}")
        else:
            print(f"team{x}")

# Problem F: Random Generator
def F():
    a, c, m, X0 = tuple(int(x) for x in input().split())
    X1 = ((a * X0) + c) % m
    
    print(X1)

# Problem G: Paper Folding
def G():
    N = int(input())
    grid = []

    for n in range(N):
        grid.append([int(x) for x in input().split()])
    
    # a simpler solution can be done.
    # by checking grid[x][y] == grid[y][x]
    def is_symmetrical(grid1, size):
        if size == 0:
            # print("No")
            return False
        if size == 1:
            # print("Yes")
            return True
        else:
            top = grid1[0]
            left = [x[0] for x in grid1]
            bottom = grid1[size-1]
            right = [x[size-1] for x in grid1]


            if top == left and bottom == right:
                if size > 2:
                    remaining = [x[1:(size-1)] for x in grid1[1:(size-1)]]
                    return is_symmetrical(remaining, len(remaining))
                return True
            else:
                # print("No")
                return False

            
    if is_symmetrical(grid, len(grid)):
        print("Yes") 
    else:
        print("No")

# Problem H: Screen Scrolling
def H():
    C, k = (int(x) for x in input().split())
    p = [int(i) for i in input().split()]

    for x in range(-k, (C-k)):
        print(p[x])

# Problem I: Is it Sorted Again?
def I():
    N = int(input())
    p = [int(i) for i in input().split()]

    if N == 1:
        print("equal")
        return 0

    inc = True
    dec = True
    eq = True

    for i in range(N):
        if i == N - 1:
            break
        else:
            if p[i] > p[i+1]: inc = False
            if p[i] < p[i+1]: dec = False
            if p[i] != p[i+1]: eq = False
    
    if eq: print("equal")
    elif inc: print("increasing")
    elif dec: print("decreasing")
    else: print("not sorted")

# Problem J: Convert
def J():
    Tc = float(input())
    Tf = (Tc * (9/5)) + 32

    print(Tf)

# Problem K: Information Tracker
def K():
    N, M = (int(x) for x in input().split())
    friends = [i for i in range(1, N + 1)]
    c = {1}

    for x in range(M):
        ab = tuple(int(i) for i in input().split())
        for s in c:
            if s in ab:
                c.update(ab)
                break

    # print(friends)
    print(len(c))

# Problem L: Lower or Higher?
def L():
    T = int(input())

    for i in range(T):
        test = input()
        a = int(test[0:test.index("is")])
        b = int(test[test.index("n ")+2:len(test)])

        if ("lower" in test) and (a < b):
            print("CORRECT")
        elif ("higher" in test) and (a > b):
            print("CORRECT")
        else:
            print("WRONG")


        # print(test, a, b)

# Problem M: Conway’s Game of Life
def M():
    R, C = (int(i) for i in input().split())
    grid = []
    # curr = 0
    for r in range(R):
        row = [int(i) for i in input().split()]
        # for x in row: curr += x
        grid.append(row)

    ans = 0
    
    for r in range(R):
        for c in range(C):
            neighbor = 0
            if r > 0: # top
                neighbor += grid[r-1][c]
            if c > 0: # left
                neighbor += grid[r][c-1]
            if r < (R-1): # bottom
                neighbor += grid[r+1][c]
            if c < (C-1): # right
                neighbor += grid[r][c+1]
            if r > 0 and c > 0: # top-left
                neighbor += grid[r-1][c-1]
            if r > 0 and c < (C-1): # top-right
                neighbor += grid[r-1][c+1]
            if r < (R-1) and c > 0: # bottom-left
                neighbor += grid[r+1][c-1]
            if r < (R-1) and c < (C-1): # bottom-right
                neighbor += grid[r+1][c+1]


            if grid[r][c] == 1:
                if neighbor in [2,3]: ans += 1
            else: # grid[r][c] == 0
                if neighbor == 3: ans += 1
    
    print(f"Alive cells: {ans}")


