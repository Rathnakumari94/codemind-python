import math
def digitsSquareSum(n):
    Sum=rem=0
    while n>0:
        rem=n%10
        Sum=Sum+math.pow(rem,2)
        n=n//10
    return Sum
n=int(input())
Temp=n
while Temp!=1 and Temp!=4:
    Temp=digitsSquareSum(Temp)
if Temp==1:
    print("True")
else:
    print("False")