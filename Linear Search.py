arr = []
def linSearch():
    flag = 0
    pos = -1
    ##print('Enter the key :- ')
    key = int(input())
    for i in range(len(arr)):
        if arr[i] == key:
            flag=1
            pos = i
            break
    if flag == 1:
        print('Element found at ',(pos+1), 'position')
    else:
        print('Element not found!!!')
        


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    linSearch()
        