# 1  2  3  4  5  6 
# 7  8  9  10 11
# 12 13 14 15
# 16 17 18
# 19 20
# 21
r=int(input())
c=1
for i in range (1,r+1):
for j in range (r+1-i):
print(c ,end=" ")
c+=1
print()
