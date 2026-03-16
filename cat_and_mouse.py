n = int(input())
arr = input().split()
d = int(input())

cats = [i for i, x in enumerate(arr) if x == 'C']
mice = [i for i, x in enumerate(arr) if x == 'M']

caught = 0
c, m = 0, 0
while c < len(cats) and m < len(mice):
    if abs(cats[c] - mice[m]) <= d:
        caught += 1
        c += 1
        m += 1
    elif cats[c] < mice[m]:
        c += 1
    else:
        m += 1

print(caught)