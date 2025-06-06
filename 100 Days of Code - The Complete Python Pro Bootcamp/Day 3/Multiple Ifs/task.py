print("Welcome to Ride")
height=float(input("What is your height in cm? "))
bill=0
if height>120:
    print("You can ride a rollercoaster...")
    age=int(input("How old are you? "))
    if age<12:
        print("Child ticket is $5 ")
        bill=5
    elif age>=12 and age<18:
        print("Your ticket is $7 ")
        bill=7
    else:
        print("Your ticket is $12 ")
        bill=12
    photo=input("do you want a photo?? Type y for yes and n for no")
    if photo=="y":
        bill+=3
        print(f"Please pay ${bill}")
    else:
        print(f"Please pay ${bill}")


else:
    print("You cannot ride it")