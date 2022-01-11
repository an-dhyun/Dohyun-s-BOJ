if __name__=="__main__":
    N = int(input())
    nums = []
    for i in range(N):
        temp = int(input())
        nums.append(temp)
    nums.sort()
    for i in nums:
        print(i)