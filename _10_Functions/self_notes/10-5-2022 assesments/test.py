num = int(input("Enter the number of rows:"))
def pascal(num):
    for i in range(num):
        print(' '* (num - i), end='')
        print(' '.join(map(str, str(11 ** i))))
pascal(num)