import sys

Left = int(sys.argv[1])
Right = int(sys.argv[2])

def UniqueCount(Left, Right):
    count = 0
    for num in range(Left, Right + 1):
        s = str(num)
        if len(s) == len(set(s)):
            count += 1
    return count

print(UniqueCount(Left, Right))