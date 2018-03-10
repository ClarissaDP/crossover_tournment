import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def balancedOrNot(expressions, maxReplacements):

    size = len(expressions)
    can_converte = []
    
    for i in range(0, size):
        expressions[i] = expressions[i].rstrip()
        
        if (expressions[i][-1] == '<'):
            can_converte.append(0)

        else:
            j = 0
            not_balanced = expressions[i].count('>') - expressions[i].count('<')

            while ( not_balanced and j < maxReplacements[i] ):
                expressions[i] = expressions[i].replace('>', '<>', 1)
                not_balanced = expressions[i].count('>') - expressions[i].count('<')
                j += 1

            if ( not_balanced == 0 ):
                can_converte.append(1)
            else:
                can_converte.append(0)

    return can_converte


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
