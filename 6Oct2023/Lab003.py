

#num1= input("Enter num1 \n")
#num1 =int{}

aList = []
print("Please Enter 5 numbers")
for i in range(0,5):
    aList.append(int(input(f"Enter {i} number:\t")))
aSet = set(aList)
print(aSet)