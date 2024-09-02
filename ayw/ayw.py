import sys

with open(sys.argv[0]) as f:
    if "import ayw as nb" in f.read():
        print("ayw NB")
    else:
        print("nb")
