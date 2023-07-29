#Add,Subtract,Multi,Div,Square,Cube,SquareRoot,CubeRoot
opt="y"
while opt.upper()=="Y":
    print("==============================================================")
    print("\nSelect any operation:")
    print('''\n1. Addtion
2. Subtraction
3. Multiplication
4. Division
5. Square of a number
6. Cube of a number
7. Square root of a number
8. Cube root of a number''')
    ch=int(input("\nEnter choice (From 1 to 8) = "))
    if ch in [1,2,3,4]:
        a=int(input("Enter the first number : "))
        b=int(input("Enter the second number : "))
        if ch==1:
            print(a,"+",b,"=", a+b)
        elif ch==2:
            print(a,"-",b,"=", a-b)
        elif ch==3:
            print(a,"*",b,"=", a*b)
        else:
            print(a,"/",b,"=", a/b)
    elif ch in [5,6,7,8]:
        c=int(input("Enter the number : "))
        if ch==5:
            print(c,end="")
            print("**2 =",c**2)
        elif ch==6:
            print(c,end="")
            print("**3 =",c**3)
        elif ch==7:
            print(c,end="")
            print("**(1/2) =",c**(1/2))
        else:
            print(c,end="")
            print("**(1/3) =",c**(1/3))
    else:
        print("Invalid option")
    opt=input("Do you wish to continue (Yes(Y) / No(Q)) : ")
print("==============================================================")    
