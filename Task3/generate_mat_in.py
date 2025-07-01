import random

def generate_matrix_line():
    rows = random.randint(5, 10)
    cols = random.randint(5, 10)
    bits = ''.join(random.choice('01') for _ in range(rows * cols))
    return f"{rows}x{cols}:{bits}"

with open("mat.in", "w") as f:
    for _ in range(100_000):
        f.write(generate_matrix_line() + "\n")

print("Fișierul mat.in a fost generat cu succes.")
