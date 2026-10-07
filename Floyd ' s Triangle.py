# Take input from the user
rows = int(input("Enter the number of rows: "))
number = 1
# Outer Loop
for i in range(1,rows+1):
    # The Inner Loop
    for j in range(1,i+1):
        print(number,end= '  ')
        number = number + 1
    print()             