import numpy as np
if __name__=="__main__":
    word = input()
    wordlist = ''.join(set(word)) # 문자열 내 중복문자 제거 방법
    countlist = []
    for i in wordlist:
        countlist.append(word.count(i))
    result = np.argmax(max(countlist))
    if countlist[result]==max(countlist): print(wordlist[result])
    else: print(-1)