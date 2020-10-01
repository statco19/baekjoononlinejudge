# 1193
n=int(input())
bound=1
cnt=1
plus=2
if n==1:
    print("1/1")
else:
    while 1:
        cnt+=1
        bound+=plus
        if n<=bound:
            k=(n-(bound-plus))-1
            # (k+1) denotes that how much n goes over LB
            # (-1 for index purpose)
            a=str(cnt-k)
            b=str(1+k)
            if cnt%2==0:
                print(b+'/'+a)
            else:
                print(a+'/'+b)
            break
        plus+=1