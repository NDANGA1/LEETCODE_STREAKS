n=10
t=True
while t:
    x=n%2
    y=n//2
    while y>1 and x>0:
        x=y%2
        y=y//2
    if x==0:
        n+=1
    else:
        t=False
        return n

