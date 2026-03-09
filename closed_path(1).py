import sys

def TotalClosedPaths(N):
    s = str(N)
    total = 0
    for char in s:
        if char in '0358':
            total += 1
        elif char == '7':
            total += 2
    return total

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n_input = int(sys.argv[1])
            print(TotalClosedPaths(n_input))
        except ValueError:
            pass