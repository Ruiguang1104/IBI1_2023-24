# a is density b is the day
# continue a=a*2 i=i+1 until a*2,<0.9
# if a>*2>0.9 break and print
a=0.05
i=1
print("the cell density on day", i,"is", a)
while a*2<0.9:
    a=a*2
    i=i+1
    print("the cell density on day", i,"is", a)
else:
    print("the maximum number of days I can have a holiday from the lab is",i)
# stop and print when a*2>=0.9
