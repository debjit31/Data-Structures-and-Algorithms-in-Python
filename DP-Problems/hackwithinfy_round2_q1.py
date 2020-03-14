#Given an array of n numbers find the largest difference in the 
#starting and ending indexes of the elements of the all possible 
#strictly decreasing sub-sequences in the array.

#Input: 21, 13, 18, 10, 7, 3, 1

#Output : 4

ar = list(map(int, input().split(',')))
n = len(ar)
all_seq = []
for i in range(n-1, -1, -1):
	ind = i
	tmp=[ar[ind]]
	while ind >= 0:
		if ar[ind-1] > ar[ind]:
			tmp.append(ar[ind-1])
		else:
			break
		ind-=1
	#print(tmp)
	if len(tmp) == 1:
		tmp = []
	else:
		all_seq.append(tmp)
#print(all_seq)
diff=[]
for i in range(len(all_seq)):
	diff.append(((max(all_seq[i])-min(all_seq[i])), i))
diff.sort(reverse = True , key = lambda x : x[0])
ie = diff[0][1]
first = all_seq[ie].index(max(all_seq[ie]))
last = all_seq[ie].index(min(all_seq[ie]))
print(first-last)
	



	