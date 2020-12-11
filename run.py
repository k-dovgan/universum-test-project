import sys

if len(sys.argv) < 2:
    sys.exit(2)
if sys.argv[1] == "pass":
    sys.exit(0)
sys.exit(1)
