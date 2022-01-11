if __name__=="__main__":
    N = int(input())
    person_dict = {}
    order = 0
    for i in range(N):
        age, name = map(str, input().split())
        person_dict[name] = [int(age), i]
    person_dict = sorted(person_dict.items(), key=lambda x:(x[1][0], x[1][1]))
    for i in person_dict: print("%d %s"%(i[1][0], i[0]))