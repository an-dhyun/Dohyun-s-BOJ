import math
if __name__=="__main__":
    N = int(input())
    list = []
    nums = input()
    for i in range(N):
        temp = int(nums.split()[i])
        check = True
        for i in range(2, int(math.sqrt(temp))):
            if temp%i==0: check = False
        if temp!=1 and check == True: list.append(temp)
    print(len(list))