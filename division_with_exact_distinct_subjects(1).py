import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(t):
        m = int(input_data[ptr])
        d = int(input_data[ptr + 1])
        ptr += 2
        
        subjects = input_data[ptr : ptr + m]
        ptr += m
        
        freq = {}
        for s in subjects:
            freq[s] = freq.get(s, 0) + 1
            
        u = len(freq)
        
        if u < d:
            results.append("0")
            continue
            
        count_2plus = 0
        for f in freq.values():
            if f >= 2:
                count_2plus += 1
        
        if 2 * d - u <= count_2plus:
            results.append("1")
        else:
            results.append("0")
            
    print(" ".join(results))

if __name__ == "__main__":
    solve()