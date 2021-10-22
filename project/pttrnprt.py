def inc(a):
    for i in range(1,a+1):print("*"*i)
def dec(a):
    for i in range(a+1,1,-1):print("*"*i)
def full(a):
     for i in range(1,a+1):print("*"*i)
     for i in range(a+1,1,-1):print("*"*i)
def pattern(a):
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print(j%2)
        print()

print("1.Increase triangle\n2.Decrease triangle\n3.Full triangle\n4.10101 pattern")
n=int(input("Enter your choice:"))
a=int(input("enter the choice:"))
pattern(5)