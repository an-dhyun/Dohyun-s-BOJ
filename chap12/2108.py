import sys
if __name__=="__main__":
    N = int(sys.stdin.readline())
    nums = []
    for i in range(N):
        nums.append(int(sys.stdin.readline()))
    # 산술평균
    print(int(round(sum(nums)/len(nums),0)))
    # 중앙값
    print(sorted(nums)[int((N-1)/2)])
    # 최빈값
    cnt = [0]*8001
    for i in nums: cnt[4000+i] += 1
    if cnt.count(max(cnt)) == 1: 
        print(cnt.index(max(cnt))-4000)
    else: # 최빈값이 여러개인 경우
        newlist = [i-4000 for i in range(len(cnt)) if cnt[i]==max(cnt)]
        newlist = [i for i in newlist if i not in [min(newlist)]] # 최소값 제거
        print(min(newlist))
    # 범위
    print(max(nums)-min(nums))