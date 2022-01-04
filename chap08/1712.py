if __name__=="__main__":
    A, B, C = map(int, input().split())
    if B>C: print(-1)
    else: 
        answer = A/(C-B)
        print(answer+1)