import sys

def check_string(s):
    n = len(s)
    for i in range(n):
        expected_count = int(s[i])
        actual_count = s.count(str(i))
        
        if actual_count != expected_count:
            return 0
    return 1

if __name__ == "__main__":
    line = input().strip()
    if line:
        print(check_string(line))