import re

print("Our Magical Calculator")
print("Type 'quit to exit\n")
previous = ""
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == "":
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("Goodbye, human")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)

        if previous == "":
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()