if __name__=="__main__":
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
    points = sorted(points, key=lambda x:(x[0], x[1]))
    for i in points:
        for j in i:
            print(j, end=' ')
        print()
        