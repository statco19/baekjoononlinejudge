def check(k,n):
	if dp[k][n] == 0:
		dp[k][n] = dp[k][n-1] + dp[k-1][n]

t = int(input())

for i in range(t):
	
	k = int(input())
	n = int(input())
	
	dp = [[0] * (n+1) for _ in range(k+1)]
	
	for j in range(1,n+1):
		dp[0][j] = j
		
	for d in range(1,k+1):
		for p in range(1,n+1):
			check(d,p)
	print(dp[k][n])
