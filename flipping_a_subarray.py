n = int(input())
arr = list(map(int, input().split()))

zeros = arr.count(0)

# max ones we can flip = max subarray sum treating 1->-1 and 0->1
transformed = [1 if x == 1 else -1 for x in arr]

max_flip = 0
curr = 0
for val in transformed:
    curr += val
    if curr < 0:
        curr = 0
    max_flip = max(max_flip, curr)

print(zeros + max_flip)