import sys
import argparse


name = sys.argv[1]
# print("hello " + name)

parser = argparse.ArgumentParser(
    description="this program prints the name of my dogs"
    )

parser.add_argument('-c','--color', metavar='color', required=True, choices={}, help="The color to search for")
args = parser.parse_args()

print(args.color)
