if __name__=="__main__":
    N = int(input())
    
    if len(str(N))<2: start = N
    else: 
        start = 10**(len(str(N))-2)
    while True: 
        if start==N: print(0); break # 없을 경우 0 출력
        sum = start # BF 시작점 설정
        for j in range(len(str(start))):
            sum += (start%(10**(j+1)))//(10**j)
        if sum==N: 
            print(start)
            break
        else: start += 1
    
