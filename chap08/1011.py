if __name__=="__main__":
    T = int(input())
    for i in range(T):
        x, y = map(int, input().split())
        length = y-x
        left = 1
        start = 2
        while True:
            if length<left*2+start: break
            else: 
                length -= (length-2*left)//start
                left += 1; start += 1
        print(length)