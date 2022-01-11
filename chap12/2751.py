import sys
if __name__=="__main__":
    
    N = int(sys.stdin.readline())
    nums = []
    for i in range(N):
        temp = int(sys.stdin.readline())
        nums.append(temp)
    nums = sorted(nums)
    for i in nums:
        print(i)