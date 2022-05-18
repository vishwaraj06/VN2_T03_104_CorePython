x=input("Enter a word to check:")
def palindrome(x):
    return x==x[::-1]
if palindrome(x):
    print("YES")
else:
    print("NO")
    