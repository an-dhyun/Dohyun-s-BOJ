import math
if __name__=="__main__":
    A, B, V = map(int, input().split())
    mid = (V-B)/(A-B)
    print(math.ceil(mid))