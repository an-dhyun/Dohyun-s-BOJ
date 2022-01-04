if __name__=="__main__":
    T = int(input())
    for i in range(T):
        H, W, N = map(int, input().split())
        if N%H==0:
            nth = N//H
            floor = H
        else: 
            nth = N//H+1
            floor = N%H
        if floor==0: floor = H
        if nth<10:
            print("%s0%s"%(floor, int(nth)))
        else:
            print("%s%s"%(floor, int(nth)))
