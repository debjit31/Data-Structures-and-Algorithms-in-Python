x = input()
y = input()
m, n = len(x), len(y)
L = [[None] *(n+1) for i in range(m+1)]
for i in range(m+1):
	for j in range(n+1):
		if i == 0 or j == 0:
			L[i][j] = 0
		elif x[i-1] == y[j-1]:
			L[i][j] = L[i-1][j-1]+1
		else:
			L[i][j] = max(L[i-1][j], L[i][j-1])
l = L[m][n]
print("LCS Length :- ", l)
lcs = [""] * (l+1)
lcs[l] = ""
i, j = m, n
while i>0 and j>0:
	if x[i-1] == y[j-1]:
		lcs[l-1] = x[i-1]
		i-=1
		j-=1
		l-=1
	elif L[i-1][j] > L[i][j-1]:
		i-=1
	else:
		j-=1
print("LCS :- ", "".join(lcs))