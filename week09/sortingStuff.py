import os

sourceDir = os.path.dirname(__file__)
filePath = os.path.join(sourceDir, "Popular_Baby_Names.csv")
f  = open(filePath)

# ignore the heading line
f.readline()


names = set()
for line in f:
    data = line.strip().split(",")
    names.add(data[3])

names = sorted(names)

for name in names:
    print(name.capitalize())

f.close