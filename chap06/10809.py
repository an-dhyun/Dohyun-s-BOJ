if __name__=="__main__":
    sentence = input()
    for i in range(97, 123):
        try:
            print(sentence.find(chr(i)), end=' ') # 특정 문자열의 위치 찾기: find()
        except:
            print(-1, end=' ')
