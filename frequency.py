import sys

def UniqueFrequencyCount(S):
    # Convert to lowercase to ensure case-insensitivity
    S = S.lower()
    
    # Store counts and track the first appearance order
    char_counts = {}
    order = []
    
    for char in S:
        if char not in char_counts:
            char_counts[char] = 1
            order.append(char)
        else:
            char_counts[char] += 1
            
    # Format each character with its count represented by '#'
    result = []
    for char in order:
        count_str = "#" * char_counts[char]
        result.append(f"{char}:{count_str}")
        
    # Join pairs with commas
    return ",".join(result)

if __name__ == "__main__":
    # Ensure S is read from command line arguments as shown in the template
    if len(sys.argv) > 1:
        S = sys.argv[1]
        print(UniqueFrequencyCount(S))