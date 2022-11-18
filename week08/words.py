import os

sourceDir = os.path.dirname(__file__)

f = os.path.join(sourceDir, 'text.txt')
g = open(os.path.join(sourceDir, "text.txt"))
lines = g.readlines

for line in lines:
    words = g.split(" ")

print(f"Words: {len(words)}")
g.close()