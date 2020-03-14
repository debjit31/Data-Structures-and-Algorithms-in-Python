import sys
n = int(input())
ar = list(map(int, input().split(sep=',')))
meh, msf = 0, -sys.maxsize-1
start, end, s = 0,0,0
start,end=0,0
for i in range(n):
	meh += ar[i]
	if meh > msf:
		msf = meh
		start=s
		end=i
	if meh < 0:
		meh=0
		s=i+1
print(msf)
print("Starting Index :- ", start, "\nEnding Index :- ", end)