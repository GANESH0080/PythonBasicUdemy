from operator import ifloordiv

obj = [2, 4, 6, 8, 10, 12]

for i in  obj:
    print(i)
    print(i*2)
print ("_____________________________________")


for j in range(1,6):
    print(j)
    if j == 3:
        print(j)
        break
print('Out of loop')
print ("_____________________________________")


k=0
for k in range(10):
    print(k)
    if k == 7:
        print(k)
        break
print('Out of loop')
print ("_____________________________________")


for n in range(1, 20, 3):
    print(n)
print ("_____________________________________")


for p in range(20):
    print(p)
print ("_____________________________________")


for r in range(10):
    if r == 7:
        print("{} {}".format("Value of r is ", r))
        continue
    print("{} {}".format("r ",r))
print ("_____________________________________")