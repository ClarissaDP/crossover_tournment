import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def rearrange(elements):
    size = elements[0] + 1
    binaries = [size]

    for i in range(1, size):
        binary = bin(elements[i]).
        binaries.append (bin(elements[i]))

    print binaries

"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()
    
    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(int(data[i]))

    result = rearrange(elements)
    
    for val in result:
        print(val)

main()
