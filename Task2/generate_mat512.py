import random

with open('mat512.in', 'w') as f:
    for _ in range(1000):  
        matrix = [str(random.randint(0, 200)) for _ in range(25)]
        f.write(' '.join(matrix) + '\n')
