import sys

filename = sys.argv[0]
f = open(filename, 'r')

lines = f.readlines()

for i in reversed(lines):
    print(i)


f.close()



