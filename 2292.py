N=int(input())
UB=1
room=1
plus=6
if N==1:
    print(1)
else:
    while 1:
        UB+=plus
        room+=1
        if N<=UB:
            print(room)
            break
        plus+=6