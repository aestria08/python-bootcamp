import art
print(art.logo)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
# print(operations["+"](9,8))

def calculator():
    wanna_continue=True
    n1=float(input("What is the first number?\n"))

    while wanna_continue:
        for symbol in operations:
            print(symbol)
        pick_operation=input("Pick one operation:")
        n2=float(input("What is the second number? \n"))
        result=operations[pick_operation](n1,n2)
        print(f"{n1}{pick_operation}{n2}={result}")

        choose=input(f"Type 'y' if want to continue with the {result}, or 'n' for new calculation\n")

        if choose=='y':
            n1=result
        else:
            wanna_continue=False
            print("\n"*15)
            calculator()

calculator()