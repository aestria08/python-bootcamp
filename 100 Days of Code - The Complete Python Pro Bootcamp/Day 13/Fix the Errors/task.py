try:
    age = int(input("How old are you?"))
except ValueError:
    print("Give numeric value please")
    age=int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You cannot drive until you turn 18")
