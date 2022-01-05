if __name__=="__main__":
    while True:
        a, b, c = map(int, input().split())
        if a==b==c==0: break
        else: 
            list = [a, b, c]
            m = list[list.index(max(list))]
            list.remove(m)
            if m**2==(list[0])**2+(list[1])**2: print("right")
            else: print("wrong")