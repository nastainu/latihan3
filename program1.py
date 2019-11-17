x=100000000
sum=0
y=0
laba = [int(0), int(0), int(x) * .1, int (x) * .1,
 int (x) * .5, int (x) * .5, int(x) * .5, int(x) * .2]
print("modal awal seorang pengusaha:", x)
for i in laba :
    sum = sum+i
    y+=1
    print("laba bulan ke-",y,"sebesar:", i)
print("total laba adalah:", sum)
