if __name__=="__main__":
    sentence = input()
    for i in range(97, 123):
        try:
            print(sentence.find(chr(i)), end=' ')
        except:
            print(-1, end=' ')
