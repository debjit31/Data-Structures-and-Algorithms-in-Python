arr = []
def bubbleSort():
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
        


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    bubbleSort()
        