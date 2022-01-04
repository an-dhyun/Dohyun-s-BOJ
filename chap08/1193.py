if __name__=="__main__":
    X = int(input())
    pointer = 1; stack = 0; line = 0; num = 0
    while True:
        stack += pointer
        if stack>=X: 
            line = pointer
            if line%2==0: 
                num = line-(stack-X)
            else: 
                num = stack-X+1
            break
        else: pointer += 1
    print("%s/%s"%(num,line+1-num))
