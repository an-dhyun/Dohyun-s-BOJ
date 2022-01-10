if __name__=="__main__":
    N = int(input())
    height = []; weight = []
    for i in range(N):
        temp = input()
        height.append(int(temp.split()[0]))
        weight.append(int(temp.split()[1]))

    ranklist = []
    for i in range(N):
        rank = 1
        for j in range(N):
            if height[i]<height[j] and weight[i]<weight[j]: rank += 1
        ranklist.append(rank)
    for i in range(len(ranklist)): 
        if i+1==len(ranklist): print(ranklist[i])
        else: print(ranklist[i], end=' ')