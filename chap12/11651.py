if __name__=="__main__":
    N = int(input())
    nums = []
    for i in range(N):
        x, y = map(int, input().split())
        nums.append([x, y])
    nums = sorted(nums, key=lambda x:(x[1], x[0]))
    for i in nums:
        for j in i:
            print(j, end=' ')
        print()
