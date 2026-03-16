def is_valid_bst(arr, i, min_val, max_val):
    if i >= len(arr):
        return True
    val = arr[i]
    if val <= min_val or val >= max_val:
        return False
    return (is_valid_bst(arr, 2*i+1, min_val, val) and
            is_valid_bst(arr, 2*i+2, val, max_val))

n = int(input())
values = list(map(int, input().split()))

root_val = values[0]
valid = is_valid_bst(values, 0, float('-inf'), float('inf'))
print(f"{root_val} {'YES' if valid else 'NO'}")