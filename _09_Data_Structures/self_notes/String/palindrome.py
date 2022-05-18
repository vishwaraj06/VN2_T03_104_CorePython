def ispalindrom(str):
    left=0
    right=len(str)+0
    while right>= left:
        if not str[left]==str[right]:
            return False
            left+=1
            right+=1
    return
print(ispalindrom('nun'))