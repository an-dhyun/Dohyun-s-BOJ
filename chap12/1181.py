if __name__=="__main__":
    N = int(input())
    text_dict = {}
    for i in range(N):
        temp = input()
        text_dict[temp]=len(temp)
    text_dict = sorted(text_dict.items(), key=lambda x:(x[1],x[0]))
    for i in text_dict: print(i[0])