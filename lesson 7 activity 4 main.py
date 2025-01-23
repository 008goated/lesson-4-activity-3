a=int(input("enter a value:"))
b=int(input("enter the value 2:"))
c=int(input("enter the value 3 :"))
average=(a+b+c)/3
print("average=",average)
if average > a and average > b and average > c:
    print("%d is higher than %d,%d,%d" %(average,a,b,c))
elif average > a  and average >b:
    print("%d is higher than %d, %d, %d" %(average,a,b,c)) 
elif average > b and average > c:
    print("%d is higher than %d,%d" %(average,b,c))
elif average > a:
    print("%d is just higher than "%(average, a))
elif average > b:
    print ("%d is ust higher than" %(average,b))
elif average > c :
    print ("%d is just higher than" %(average,c))
else:print("invalid input")