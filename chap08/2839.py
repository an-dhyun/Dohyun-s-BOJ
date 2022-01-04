if __name__=="__main__":
    N = int(input())
    three = 0; five = 0
    for i in range(0,int(N//5)+1):
        if (N-(i*5))%3==0:
            five = i; three = (N-(i*5))//3
    if three==0 and five==0: print(-1)
    else: print(three+five)