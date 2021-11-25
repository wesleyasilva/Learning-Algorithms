array = [1,6,8,9,12,14,17,20,27,30,39]

x = int(input("Type your lucky number: "))
exist = False

while exist == False:
    for b in array:
        if x == b:
            print("Yeah! Your number is on the list.")
            exist = True

    if exist == False:
        print("Oh No! Your number isn´t on the list.\n")
        x = int(input("Try Again: "))

