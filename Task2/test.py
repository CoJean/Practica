import os
import time
from multiprocessing import Pool

input_dir = 'input'
output_dir_seq = 'output_seq'
output_dir_par = 'output_par'

os.makedirs(output_dir_seq, exist_ok=True)
os.makedirs(output_dir_par, exist_ok=True)

def process_file_sequential(filename):
    input_path = os.path.join(input_dir, filename)
    output_filename = filename.replace('.in', '.out')
    output_path = os.path.join(output_dir_seq, output_filename)

    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
        for line in fin:
            fout.write(line)

def process_file_parallel(filename):
    input_path = os.path.join(input_dir, filename)
    output_filename = filename.replace('.in', '.out')
    output_path = os.path.join(output_dir_par, output_filename)

    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
        for line in fin:
            fout.write(line)

def process_files_sequential():
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.in')]
    for f in input_files:
        process_file_sequential(f)

def process_files_parallel():
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.in')]
    with Pool() as pool:
        pool.map(process_file_parallel, input_files)

def main():
    # Ruleaza secvential
    start_seq = time.time()
    process_files_sequential()
    end_seq = time.time()
    time_seq = end_seq - start_seq

    # Ruleaza paralel
    start_par = time.time()
    process_files_parallel()
    end_par = time.time()
    time_par = end_par - start_par

    # Scrie raportul
    with open('task-mat-cache-parallel-testing.txt', 'w') as f:
        f.write("Comparatie performanta: secvential vs paralel\n\n")
        f.write(f"Timp secvential: {time_seq:.2f} secunde\n")
        f.write(f"Timp paralel: {time_par:.2f} secunde\n")
        f.write(f"Speedup: {time_seq/time_par:.2f}x\n")

    print("Test complet. Vezi fisierul task-mat-cache-parallel-testing.txt")

if __name__ == '__main__':
    main()
