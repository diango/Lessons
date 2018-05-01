from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
# in_file = open(from_file, "r")
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exists {len(to_file)}")
print("Ready, hit Return or CTRL-C to quit")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("All right all done")

out_file.closed
in_file.close()