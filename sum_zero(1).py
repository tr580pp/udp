import sys

Marks = [int(x) for x in sys.argv[1].split(',')]

def SumZero(Marks):
    count = 0
    n = len(Marks)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += Marks[j]
            if current_sum == 0:
                count += 1
    return count

print(SumZero(Marks))