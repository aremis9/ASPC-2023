# ANSWERS TO ASPC-A FINAL
# https://github.com/aremis9/ASPC-2023/blob/main/ASPCA-Review-of-Basics/Finals.pdf


# Problem A: AM-GM Inequality
from re import L


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
    
