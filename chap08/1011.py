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
                temp_len = length
                length -= (length-2*left)//start
                start += 1
                (temp_len-length)/start
        print(length)