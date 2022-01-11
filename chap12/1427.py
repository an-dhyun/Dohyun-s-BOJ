import sys
if __name__=="__main__":
    N = input()
    nums = sorted([int(N[i]) for i in range(len(N))], reverse=True)
    for i in nums: print(i, end='')