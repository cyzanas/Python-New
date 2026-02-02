math=input("Expression: ").strip()
x,y,z=math.split()
x=int(x)
z=int(z)
if y=="+":
    sum=x+z
    print(float(sum))
elif y=="-":
    sum=x-z
    print(float(sum))
elif y=="*":
    sum=x*z
    print(float(sum))
elif y=="/":
    sum=x/z
    print(float(sum))
else:
    print("it's an math interpreter")
    
    