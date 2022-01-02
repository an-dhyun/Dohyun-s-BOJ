if __name__=="__main__":
    T = int(input())
    for i in range(T):
        R, S = input().split()
        for i in range(len(S)-1): print(S[i]*int(R), end='')
        print(S[len(S)-1]*int(R))