import os
from multiprocessing import Pool

input_dir = 'input'    
output_dir = 'output'  

os.makedirs(output_dir, exist_ok=True)

def process_file(filename):
    input_path = os.path.join(input_dir, filename)
    output_filename = filename.replace('.in', '.out')
    output_path = os.path.join(output_dir, output_filename)

    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
        for line in fin:
            
            fout.write(line)

    return f'Processed {filename}'

def main():
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.in')]

    with Pool() as pool:
        results = pool.map(process_file, input_files)

    for r in results:
        print(r)

if __name__ == '__main__':
    main()
