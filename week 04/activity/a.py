for i in range(1,8):
    for j in range(7,i,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print('\n')