if __name__=="__main__":
    M, N = map(int, input().split())
    list = [True for x in range(0, N+1)]
    list[0]=list[1]=False
    for i in range(2, int(N**0.5)+1):
        for j in range(i*i,N+1,i):
            list[j] = False
    for i in range(M,N+1): 
        if list[i]==True: print(i)