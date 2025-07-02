import random

def generate_random_matrix(rows, cols):
    return ''.join(random.choice('01') for _ in range(rows * cols))

def generate_mat_in(filename, num_lines=1000, min_size=5, max_size=10):
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            rows = random.randint(min_size, max_size)
            cols = random.randint(min_size, max_size)
            matrix_data = generate_random_matrix(rows, cols)
            line = f"{rows}x{cols}:{matrix_data}\n"
            f.write(line)

if __name__ == "__main__":
    generate_mat_in('mat.in', num_lines=1000, min_size=5, max_size=10)
    print("Fisierul 'mat.in' a fost generat cu 1000 linii.")
