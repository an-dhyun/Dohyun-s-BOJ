if __name__=="__main__":
    sentence = input()
    print(sentence.find("lj"))
    if sentence.find("c=") != -1: sentence = sentence.replace("c=","x")
    if sentence.find("c-") != -1: sentence = sentence.replace("c-","x")
    if sentence.find("dz=") != -1: sentence = sentence.replace("dz=","x")
    if sentence.find("d-") != -1: sentence = sentence.replace("d-","x")
    if sentence.find('lj') != -1: sentence = sentence.replace("lj","x")
    if sentence.find("nj") != -1: sentence = sentence.replace("nj","x")
    if sentence.find("s=") != -1: sentence = sentence.replace("s=","x")
    if sentence.find("z=") != -1: sentence = sentence.replace("z=","x")
    print(len(sentence))
    
