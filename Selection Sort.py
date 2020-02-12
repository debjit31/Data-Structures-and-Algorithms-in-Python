a = []
def selectionSort():
    for i in range(0, len(a)):
        pos = i
        for j in range(i+1, len(a)):
            if a[pos] > a[j]:
                pos = j
        if pos!=i:
            a[pos], a[i] = a[i], a[pos]
    print(a)
        


if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    selectionSort()
        