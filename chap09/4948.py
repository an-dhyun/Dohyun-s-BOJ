if __name__=="__main__":
    while True:
        N = int(input())
        if N==0: break
        result = 0
        for i in range(N+1, 2*N+1):
            check = True
            for j in range(2,int(i**0.5)+1):
                if i%j==0: check = False
            if i!=0 and check == True: result += 1
        print(result)