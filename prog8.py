# A
# BC
# DEF
# GHIJ
# KLMNO
# PQRSTU
r=int(input())
c=65
for i in range (1,r+1):
for j in range (i):
print(chr(c),end="")
c+=1
print()
