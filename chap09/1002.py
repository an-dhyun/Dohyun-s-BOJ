import math
if __name__=="__main__":
    T = int(input())
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        # 교점이 무한대로 많은 경우: 일치
        if x1==x2 and y1==y2 and r1==r2: print(-1)
        # 교점이 0개인 경우: 중심사이거리>반지름합, 중심일치/반지름일치x
        elif math.sqrt((x1-x2)**2)+math.sqrt((y1-y2)**2)>r1+r2 or (x1==x2 and y1==y2 and r1!=r2): print(0)
        # 교점이 하나인 경우: 중심사이거리=반지름합, 중심사이거리+작은반지름=큰반지름
        elif math.sqrt((x1-x2)**2)+math.sqrt((y1-y2)**2)==r1+r2 or math.sqrt((x1-x2)**2+(y1-y2)**2)+min(r1, r2)==max(r1, r2): print(1)
        # 교점이 두개인 경우: 중심사이거리=큰반지름, 중심사이거리<반지름합
        elif (x1-x2)**2+(y1-y2)**2==min(r1,r2)**2 or math.sqrt((x1-x2)**2+(y1-y2)**2)<r1+r2: print(2)
        