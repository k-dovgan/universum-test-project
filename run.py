#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("Unknown outcome")
    sys.exit(2)
if sys.argv[1] == "pass":
    print("Script succeeded")
    sys.exit(0)
print("Script failed")
sys.exit(1)
