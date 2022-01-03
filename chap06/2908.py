import math
if __name__=="__main__":
    A, B = input().split()
    reA = 0; reB = 0
    for i in range(3): reA += int(A[2-i]) * math.pow(10,2-i)
    for i in range(3): reB += int(B[2-i]) * math.pow(10,2-i)
    print(max([reA, reB]))