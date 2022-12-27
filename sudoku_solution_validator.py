def valid_solution(board):
    a1 = sorted(list(board[0][0:3]+board[1][0:3]+board[2][0:3]))
    b1 = sorted(list(board[3][0:3]+board[4][0:3]+board[5][0:3]))
    c1 = sorted(list(board[6][0:3]+board[7][0:3]+board[8][0:3]))
    a2 = sorted(list(board[0][3:6]+board[1][3:6]+board[2][3:6]))
    b2 = sorted(list(board[3][3:6]+board[4][3:6]+board[5][3:6]))
    c2 = sorted(list(board[6][3:6]+board[7][3:6]+board[8][3:6]))
    a3 = sorted(list(board[0][6:9]+board[1][6:9]+board[2][6:9]))
    b3 = sorted(list(board[3][6:9]+board[4][6:9]+board[5][6:9]))
    c3 = sorted(list(board[6][6:9]+board[7][6:9]+board[8][6:9]))
    d1 = sorted(list(board[0]))
    d2 = sorted(list(board[1]))
    d3 = sorted(list(board[2]))
    d4 = sorted(list(board[3]))
    d5 = sorted(list(board[4]))
    d6 = sorted(list(board[5]))
    d7 = sorted(list(board[6]))
    d8 = sorted(list(board[7]))
    d9 = sorted(list(board[8]))
    e1 = sorted(list(str(board[0][0])+str(board[1][0])+str(board[2][0])+str(board[3][0])+str(board[4][0])+str(board[5][0])+str(board[6][0])+str(board[7][0])+str(board[8][0])))
    e2 = sorted(list(str(board[0][1])+str(board[1][1])+str(board[2][1])+str(board[3][1])+str(board[4][1])+str(board[5][1])+str(board[6][1])+str(board[7][1])+str(board[8][1])))
    e3 = sorted(list(str(board[0][2])+str(board[1][2])+str(board[2][2])+str(board[3][2])+str(board[4][2])+str(board[5][2])+str(board[6][2])+str(board[7][2])+str(board[8][2])))
    e4 = sorted(list(str(board[0][3])+str(board[1][3])+str(board[2][3])+str(board[3][3])+str(board[4][3])+str(board[5][3])+str(board[6][3])+str(board[7][3])+str(board[8][3])))
    e5 = sorted(list(str(board[0][4])+str(board[1][4])+str(board[2][4])+str(board[3][4])+str(board[4][4])+str(board[5][4])+str(board[6][4])+str(board[7][4])+str(board[8][4])))
    e6 = sorted(list(str(board[0][5])+str(board[1][5])+str(board[2][5])+str(board[3][5])+str(board[4][5])+str(board[5][5])+str(board[6][5])+str(board[7][5])+str(board[8][5])))
    e7 = sorted(list(str(board[0][6])+str(board[1][6])+str(board[2][6])+str(board[3][6])+str(board[4][6])+str(board[5][6])+str(board[6][6])+str(board[7][6])+str(board[8][6])))
    e8 = sorted(list(str(board[0][7])+str(board[1][7])+str(board[2][7])+str(board[3][7])+str(board[4][7])+str(board[5][7])+str(board[6][7])+str(board[7][7])+str(board[8][7])))
    e9 = sorted(list(str(board[0][8])+str(board[1][8])+str(board[2][8])+str(board[3][8])+str(board[4][8])+str(board[5][8])+str(board[6][8])+str(board[7][8])+str(board[8][8])))
    ans = 0
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if a1==arr:
        ans+=1
    if a2 == arr:
        ans += 1
    if a3==arr:
        ans+=1
    if b1==arr:
        ans+=1
    if b2==arr:
        ans+=1
    if b3==arr:
        ans+=1
    if c1==arr:
        ans+=1
    if c2==arr:
        ans+=1
    if c3==arr:
        ans+=1
    if d1==arr:
        ans+=1
    if d2==arr:
        ans+=1
    if d3==arr:
        ans+=1
    if d4==arr:
        ans+=1
    if d5==arr:
        ans+=1
    if d6==arr:
        ans+=1
    if d7==arr:
        ans+=1
    if d8==arr:
        ans+=1
    if d9==arr:
        ans+=1
    if e1==arr2:
        ans+=1
    if e2==arr2:
        ans+=1
    if e3==arr2:
        ans+=1
    if e4==arr2:
        ans+=1
    if e5==arr2:
        ans+=1
    if e6==arr2:
        ans+=1
    if e7==arr2:
        ans+=1
    if e8==arr2:
        ans+=1
    if e9==arr2:
        ans+=1
    if ans == 27:
        return True
    return False
print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                    ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
