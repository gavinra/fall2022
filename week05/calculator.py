import math

def printComputation(kind, value, answer):
    print(f"The {kind} of {value} is {answer}")

print("Pick an operation: ")
print(" sine")
print(" cosine")
print(" tangent")

selection = input("Your choice: ")
if selection in ("sine", "cosine", "tangent", "Sine", "Cosine", "Tangent"):
    value = float(input("Enter the angle, in radians: "))
    if selection == "sine":
        printComputation(selection, value, math.sin(value))
    elif selection == "cosine":
        printComputation(selection, value, math.cos(value))
    elif selection == "tangent":
        printComputation(selection, value, math.tan(value))
    elif selection == "Sine":
        printComputation(selection, value, math.sin(value))
    elif selection == "Cosine":
        printComputation(selection, value, math.cos(value))
    elif selection == "Tangent":
        printComputation(selection, value, math.tan(value))
else:
    print("Just plain unacceptable.")
