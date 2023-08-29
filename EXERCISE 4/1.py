def pangram(n):
    for x in range(26):
        if chr(x+97) not in n:
            return False
        else:
            return True
n = "The quick brown fox jumps over a lazy dog"
if pangram(n):
    print(True)
else:
    print(False)
