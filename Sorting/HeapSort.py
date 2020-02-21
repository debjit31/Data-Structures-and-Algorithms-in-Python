def heapify(arr, n, i):
    root = i
    lc = 2*i + 1
    rc = 2*i + 2
    if lc < n and arr[root] < arr[lc]:
        root = lc
    if rc < n and arr[root] < arr[rc]:
        root = rc
    
    if root != i:
        arr[root] , arr[i] = arr[i], arr[root]
        heapify(arr, n, root)

def heapSort():
    n = len(arr)
    ##Heapify Operation
    for i in range(n, -1, -1):
        heapify(arr,n,i)
        
    ##Extraction Operation
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    heapSort()
    print(arr)