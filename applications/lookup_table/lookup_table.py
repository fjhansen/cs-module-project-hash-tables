# Your code here
import random
import math

catche = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# catche should always be global



def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    key = (x,y)
    #print("\n KEY: \n", key)

    if key not in catche:
        catche[key] = slowfun_too_slow(x,y)
    #print("\n CATCHE_KEY: \n",catche)
    return catche[key]
    

##
##for i in range(10):
##    x = random.randrange(2, 14)
##    y = random.randrange(3, 6)
##    print(f'\n index_{i}_key_val: {x},{y}: {slowfun(x, y)} \n')



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
