import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def balancedOrNot(expressions, maxReplacements):
    return [1, 0]

"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()
    
    
    expressionsCount = int(data[0])
    expressions = []

    for i in range(1, expressionsCount + 1):
        expressions.append(data[i])
    
    maxReplacementsCount = int(data[expressionsCount + 1])
    maxReplacements = []
    
    for i in range(expressionsCount + 2, len(data)):
        maxReplacements.append(int(data[i]))

    result = balancedOrNot(expressions, maxReplacements)
    
    for val in result:
        print(val)

main()
