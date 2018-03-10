import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def rearrange(elements):

    size = len(elements)
    binaries = []
    for element in elements:
        binary = bin(element).split('b')[1]
        bin_ones = binary.count("1")
        binaries.append(bin_ones)

    ordered = []
    quant = list(set(binaries))
    for i in range(0, len(quant)):
        same_bin = [j for j, x in enumerate(binaries) if x == quant[i]]
        
        if ( len(same_bin) == 1 ):
            ordered.append(binaries[same_bin[0]])
        else:
            for j in same_bin:
                add = j
                for k in same_bin:
                    if ( (elements[add] in ordered or elements[k] < elements[add]) and (elements[k] not in ordered) ):
                        add = k
                ordered.append(elements[add])

    return ordered


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
