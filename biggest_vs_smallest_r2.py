largest = None
smallest = None
count = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    try:
        num = float(num) 
        count = count + 1
        if count == 1:
             largest = num
             smallest = num
             
        else : 
            if num > largest :
             largest = num
             
            elif num < smallest :
                smallest = num
                
            else :
                continue
    except :
        print("Invalid input")
        





print("Maximum is ", int(largest))
print("Minimum is ", int(smallest))