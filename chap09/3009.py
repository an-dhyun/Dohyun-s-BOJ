if __name__=="__main__":
    x = []; y = []
    for i in range(3):
        a, b = map(int, input().split())
        x.append(a); y.append(b)
    w = max(x)-min(x); h = max(y)-min(y)
    print(max(x)*2+min(x)*2-sum(x),max(y)*2+min(y)*2-sum(y))