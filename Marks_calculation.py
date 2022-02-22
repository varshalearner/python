#max percentage must not exceed 82%
sub1=int(input("Enter marks of subject 1 : "))
sub2=int(input("Enter marks of subject 2 : "))
sub3=int(input("Enter marks of subject 3 : "))
sub4=int(input("Enter marks of subject 4 : "))
print("Marks of subject 5:")
if(410-sub1-sub2-sub3-sub4<(410*0.82)):
    print("0 to ",410-sub1-sub2-sub3-sub4)
else:
    print("0 to 100")
