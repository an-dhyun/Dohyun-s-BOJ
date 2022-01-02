if __name__=="__main__":
    a = int(input())
    nums = input()
    answer = 0
    for i in range(a):
        answer += int(nums[i])
    print(answer)    