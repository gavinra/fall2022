score = 0
print("You will receive one point for every question you answer correctly")
answer = input("What color is the sky? ")
if answer == "blue":
    score = score + 1
    print("Yes!")
elif answer == "Blue":
    score = score + 1
    print("Yes!")
else:
     print("I was looking for 'blue'.")
answer = input("How old is the president? ")
if answer == "79":
    print("Good.")
    score = score + 1
elif answer == "seventy-nine":
    score = score + 1
    print("Good.")
else:
    print("Nope.")
answer = input("How many Great Lakes are there? ")
if answer == "5":
    score = score + 1
    print("Oh, you are smart!")
elif answer == "five":
    score = score + 1
    print("Oh, you are smart!")
elif answer == "Five":
    score = score + 1
    print("Oh, you are smart!")
else:
    print("Nice try.")
print("Your score is", score)
 