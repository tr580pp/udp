import sys

def MagicString(S):
    count_m = S.count('m')
    count_o = S.count('o')
    count_n = S.count('n')
    count_p = S.count('p')
    
    if (count_m + count_o) % 2 == 0 and (count_n + count_p) % 2 == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    try:
        line = input().strip()
        if line:
            print(MagicString(line))
    except EOFError:
        pass