import sys

args = sys.argv

if len(args) < 2:
    exit(1)

inpath = args[1]

fout = open("output.txt", "wb")

def writeline(fout, str):
    fout.write(bytes(str + "\n", "UTF-8"))

with open(inpath, "rb") as fin:
    for line in fin:
        line = line.strip().decode("UTF-8")
        writeline(fout, line)

fout.close()

