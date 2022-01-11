if __name__=="__main__":
    N = int(input())
    nums = [0]*2000000001
    temp = input()
    inp = []
    for i in range(N):
        here = int(temp.split()[i])
        inp.append(here)
        nums[here+1000000000] += 1
    for i in inp:
        print(sum(nums[:here+1000000000]), end=' ')
    
