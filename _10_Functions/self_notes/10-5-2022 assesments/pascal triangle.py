def pascal(n):
    result=[]
    for i in range(1,n+1):
        row=[]
        for j in range(1,i+1):
            elem=1
            if j==1 or j==i:
                elem=1
            else:
                curRow=i-1
                preRow=curRow-1
                curPos=j-1
            elem=result[preRow][curPos-1]+result[preRow][curPos]
            row.append((elem))
        result.append(row)
    return result
print(pascal(7))


