import random

d = ("'yes'")
e = ("'no'")
f = ("'not sure'")
g = ("could")
h = ("should")
i = ("would")
j = ("What")
k = ("Is there a")
l = ("Do you have a")

number = 1  #number is the variable that keeps track of the problem number

n = {"A: Yes": d, "B: No": e, "C: Not Sure": f}
o = {"A: could": g, "B: should":h, "C: would": i}
p = {"A: What": j, "B: Is there a": k, "C: Do you have a":l}

questions= [
    (
f"Did Question 1 make sense?", n
),
    (
f"Which of these words do you pick?", o
),
    (
f"Which of the following intrigues you?", p
)
]

random.shuffle(questions)

l4 = []

for s in questions:
    iter(s[1])
    u = s[1]
    for t in u:
        l4.append(u[t])


a = (questions[0])
b = (questions[1])
c = (questions[2])

m = {"A: Question 2": a, "B: Question 3": b,"C: Question 4": c}

question1 = (
    f"What question do you want to answer next?", m
)

print(f"Question {number}:")
print(question1[0])

for g in question1[1]:
    print(g)

i = input("Type 'A', 'B', or 'C' to choose your answer. When you're finished, press 'Enter' ")
print(" ")

if i == 'B':
    print(f"As much as I'd like to let you answer Question 3 right now, I'll let you answer Question 2, folks.")
    print(" ")
elif i == 'C':
    print("Even though I'd really enjoy letting you answer Question 4, let's stick to Question 2 for now, folks.")
    print(" ")

l1 = ["a", "b", "c", "d"]
l2 = []
count = -1
v = d
w = e
x = f
quantity = -1
variable = -1
a1 = -3
a2 = -2
a3 = -1

for z in questions:
    number += 1
    variable += 1
    a1 += 3
    a2 += 3
    a3 += 3
    for y in range(0,3):
        count += 1
        quantity += 1
        l1[quantity] = l4[count]
    v = l4[a1]
    w = l4[a2]
    x = l4[a3]
    print(f"Question {number}:")
    print(z[0])
    for q in z[1]:
        print(q)
    r = input("Type 'A', 'B', or 'C' to choose your answer. When you're finished, press 'Enter' ")
    if r == 'A':
        l2.append(v)
    elif r == 'B':
        l2.append(w)
    elif r == 'C':
        l2.append(x)
    print(" ")
    quantity = -1
print("Here are the answers you submitted, in word form this time, folks:")
print(l2)
