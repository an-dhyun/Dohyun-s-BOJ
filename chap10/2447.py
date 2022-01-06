def star(style):
    style = [[style, style, style], [style, ' ', style], [style, style, style]]
    return style

def printstar(input):
    # print(len(input))
    # print(input)
    # print(len(input[0]))
    # print(input[0])
    # print(len(input[0][0]))
    # print(input[0][0])
    for f in range(3):
        for e in range(3):
            for d in range(3):
                for c in range(3):
                    for b in range(3):
                        for a in range(3):
                            try: 
                                print(input[f][e][d][c][b][a],end='')
                            except: print(' ', end='')
                        print('')
                    print('')
                print('')
            print('')
        print('')

if __name__=="__main__":
    # N = int(int(input())**(1/3))
    # N = 0
    # for i in range(int(1)):
    #     start = star(start)
    style = star("*")
    # for i in range(1):
    #     style = star(style)
    printstar(star(star(style)))