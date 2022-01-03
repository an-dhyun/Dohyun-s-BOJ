def find(word, target):
    answer = []
    index = -1
    check = True
    while True:
        index = word.find(target, index + 1)
        if index == -1: break
        else: answer.append(index)
    for i in range(len(answer)-1):
        if answer[i+1]-answer[i] != 1: check = False
    return check

if __name__=="__main__":
    T = int(input())
    count = 0
    for i in range(T):
        word = input()
        check = True
        for i in word:
            if word.count(i) != 1 and find(word, i)==False: check = False
        if check==True: count += 1
    print(count)