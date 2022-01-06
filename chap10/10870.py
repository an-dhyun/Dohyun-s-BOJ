def fibona(first, second):
    temp = first
    first = second
    second = temp+second
    return first, second

if __name__=="__main__":
    n = int(input())
    if n==0: print(0)
    else:
        first = 0; second = 1
        for i in range(n-1):
            first, second = fibona(first, second)
        print(second)
