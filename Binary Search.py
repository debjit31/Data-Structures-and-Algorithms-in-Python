arr = []
def binarySearch (low, high, key): 
	if high >= low: 
		mid = low + (high - low)//2
		if arr[mid] == key: 
			return mid 
		elif arr[mid] > key: 
			return binarySearch(low, mid-1, key) 
		else: 
			return binarySearch(mid+1, high, key) 
	else: 
		return -1

print('Enter the elements in the array :- ')
arr = [int(x) for x in input().split()] 
arr.sort()
key = int(input())
result = binarySearch(0, len(arr)-1, key) 

if result != -1: 
	print ("Element is present at index %d" % (result+1))
else: 
	print ("Element is not present in array")
