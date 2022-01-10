if __name__=="__main__":
    # 입력본 제작
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        temp = []
        tmp_input = input()
        for j in range(M):
            temp.append(tmp_input[j])
        board.append(temp)
    
    # 견본 제작
    first_pane = [] # W로 시작
    second_pane = [] # B로 시작
    for i in range(N):
        temp_f = []
        temp_s = []
        if i%2==0: 
            for j in range(0,M):
                if j%2==0: 
                    temp_f.append("W")
                    temp_s.append("B")
                else:
                    temp_f.append("B")
                    temp_s.append("W")
        else: 
            for j in range(0,M):
                if j%2==0: 
                    temp_f.append("B")
                    temp_s.append("W")
                else:
                    temp_f.append("W")
                    temp_s.append("B")
        first_pane.append(temp_f)
        second_pane.append(temp_s)

    # 값 매기기
    result = []
    # print(M, N)
    for i in range(N-8+1):
        for j in range(M-8+1):
            first_value = 0
            second_value = 0
            # rint(i, j)
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if board[a][b]!=first_pane[a][b]: first_value += 1
                    if board[a][b]!=second_pane[a][b]: second_value += 1
            # print(min(first_value, second_value))
            result.append(min(first_value, second_value))
    print(min(result))