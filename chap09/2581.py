import math
if __name__=="__main__":
    M = int(input())
    N = int(input())
    list = []
    for i in range(M, N+1):
        check = True
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0: check = False
        if i!=1 and check==True: list.append(i)
    if len(list) != 0:
        print(sum(list))
        print(min(list))
    else:
        print(-1)