import numpy as np
if __name__=="__main__":
    word = input().upper()
    wordlist = list(set(word)) # 문자열 내 중복문자 제거 방법
    countlist = []
    for i in wordlist:
        countlist.append(word.count(i))
    if countlist.count(max(countlist)) == 1: 
        max_idx = countlist.index(max(countlist))
        print(wordlist[max_idx])
    else: print('?')