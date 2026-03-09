import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    nums = list(map(int, input_data[1:n+1]))
    k = int(input_data[n+1])

    if k < 0:
        print(0)
        return

    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    unique_pairs = 0
    
    if k == 0:
        for val in counts:
            if counts[val] > 1:
                unique_pairs += 1
    else:
        for val in counts:
            if val + k in counts:
                unique_pairs += 1

    print(unique_pairs)

if __name__ == "__main__":
    solve()