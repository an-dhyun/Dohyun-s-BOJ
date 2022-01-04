if __name__=="__main__":
    T = int(input())
    for i in range(T):
        k = int(input())
        n = int(input())
        result = 0
        list = [x for x in range(1, n+1)]
        if k==1:
            result += sum(list)
        if k>1:
            for i in range(1,k):
                templist = list.copy()
                for j in range(1,n):
                    for a in range(j):
                        list[j] = sum(templist[0:j+1])
            result += sum(list)
        print(result)