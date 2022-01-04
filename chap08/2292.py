if __name__=="__main__":
    N = int(input())
    pointer = 1; stack = 0; line = 0
    while True:
        pointer += stack*6
        if N<=pointer: 
            line = stack+1
            break
        else: stack += 1
    print(line)