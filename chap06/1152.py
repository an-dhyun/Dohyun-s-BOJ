if __name__=="__main__":
    sent = input().split()
    try: sent.remove('')
    except: exit
    print(len(sent))