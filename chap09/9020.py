if __name__=="__main__":
    list = [True for x in range(0, 10001)]
    list[0]=list[1]=False
    for i in range(2, int(10000**0.5)+1):
        for j in range(i*i,10001,i):
            list[j]=False
    T = int(input())
    for i in range(T):
        n = int(input())
        first = 0; second = 0
        for i in range(n//2, n+1):
            if list[i]==True and list[n-i]==True:
                first = n-i; second = i; break
        print(first, second)