m = int(input())
list1 = list(map(int, input().split()))
n = int(input())
list2 = list(map(int, input().split()))

num1 = int("".join(map(str, list1[::-1])))
num2 = int("".join(map(str, list2[::-1])))

total = num1 + num2

result = [int(d) for d in str(total)][::-1]
print(" ".join(map(str, result)))