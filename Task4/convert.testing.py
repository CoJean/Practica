import subprocess
import time

def run_convert(input_file, cache_size=None):
    cmd = ["go", "run", "convert.go", input_file]
    if cache_size is not None:
        cmd.append(str(cache_size))  # presupunem că programul Go acceptă parametru cache size
    start = time.time()
    subprocess.run(cmd, check=True)
    end = time.time()
    return end - start

def main():
    input_file = "mat.in"
    input_file_x = "mat.in.x"

    with open("convert-testing.txt", "w") as f:
        f.write("Comparație performanță convertor Go\n")
        f.write("-----------------------------------\n")

        # Fără cache
        time_no_cache = run_convert(input_file)
        f.write(f"Timp fără cache (mat.in): {time_no_cache:.4f} secunde\n")

        time_no_cache_x = run_convert(input_file_x)
        f.write(f"Timp fără cache (mat.in.x): {time_no_cache_x:.4f} secunde\n\n")

        # Cu cache 100
        time_cache_100 = run_convert(input_file, cache_size=100)
        f.write(f"Timp cu cache 100 intrări (mat.in): {time_cache_100:.4f} secunde\n")

        time_cache_100_x = run_convert(input_file_x, cache_size=100)
        f.write(f"Timp cu cache 100 intrări (mat.in.x): {time_cache_100_x:.4f} secunde\n\n")

        # Cu cache 1000
        time_cache_1000 = run_convert(input_file, cache_size=1000)
        f.write(f"Timp cu cache 1000 intrări (mat.in): {time_cache_1000:.4f} secunde\n")

        time_cache_1000_x = run_convert(input_file_x, cache_size=1000)
        f.write(f"Timp cu cache 1000 intrări (mat.in.x): {time_cache_1000_x:.4f} secunde\n")

if __name__ == "__main__":
    main()
