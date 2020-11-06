print('Calculator')
print('Enter the two numbers that you want to add,subtract,multiply or divide')
x=float(input('Enter the first number'))
y=float(input('Enter the second number'))
print('Selections:')
print('Press 1 to add')
print('Press 2 to subtract')
print('Press 3 to multiply')
print('Press 4 to divide')
choice=int(input('Enter your selection'))
    
if choice==1:
    result=round((x+y),3)
    print('The result is',result)
    
elif choice==2:
    result=round((x-y),3)
    print('The result is',result)
    
elif choice==3:
    result=round((x*y),3)
    print('The result is',result)
    
elif choice==4:
    result=round((x/y),3)
    print('The result is',result)
    
elif choice>=4:
    print('Invalid option')
    
elif choice<=1:
    print('Invalid option')
    
#This is the code of a calculator app.
