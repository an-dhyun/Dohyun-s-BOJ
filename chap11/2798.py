if __name__=="__main__":
    N, M = map(int, input().split())
    list = []
    temp = input()
    for i in range(N):
        list.append(int(temp.split()[i]))
    
    result = 0
    for i in range(len(list)-2):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if result< list[i]+list[j]+list[k] <=M: 
                    result = list[i]+list[j]+list[k]
    print(result)