import random

with open('mat96.in', 'w') as f:
    for _ in range(100): 
        matrix = [str(random.randint(0, 100)) for _ in range(25)]
        f.write(' '.join(matrix) + '\n')
