n=input().split(",")
res=[]
for num in n:
    decimal=int(num,2)
    if(decimal%5==0):
        res.append(num)
print(",".join(res))