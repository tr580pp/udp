import sys

def AnagramCheck(Str1, Str2):
    if len(Str1) != len(Str2):
        return "Not Anagram"
    
    if sorted(Str1) == sorted(Str2):
        return "Anagram"
    else:
        return "Not Anagram"

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        Str1 = sys.argv[1]
        Str2 = sys.argv[2]
        print(AnagramCheck(Str1, Str2))