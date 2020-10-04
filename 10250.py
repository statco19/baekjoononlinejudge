t = int(input())
for i in range(t):
    h,w,n = map(int,input().split())
    if n % h == 0:
        XX = n // h
    else:
        XX = n//h + 1
    if XX < 10:
        XX = '0' + str(XX)
    else:
        XX = str(XX)
    
    if n % h == 0:
        YY = str(h)
    else:
        YY = str(n - (n // h) * h)
        
    print(YY + XX)