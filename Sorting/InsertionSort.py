def insertionSort():
    for i in range(1, len(a)):
        j=i-1
        while j >= 0 and a[i] < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1]= a[i]



if __name__ == '__main__':
    a=[]
    a = [int(x) for x in input().split()]
    insertionSort()
    print(a)