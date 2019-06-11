t=int(input())
while(t):
    print(".".join(input().split(".")[::-1]))
    t-=1
