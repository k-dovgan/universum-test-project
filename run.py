
#!/usr/bin/env python

import sys

with open("execution.log", "w+") as new_file:
    new_file.write("Here's what a script accepted from command line:\n" + str(sys.argv))

if len(sys.argv) < 2:
    print("Unknown outcome")
    sys.exit(2)
if sys.argv[1] == "pass":
    print("Script succeeded")
    sys.exit(0)
print("Script failed")
sys.exit(1)
