import subprocess
import time

def run_and_time(command):
    start = time.perf_counter()
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL)
    end = time.perf_counter()
    return round(end - start, 4)

def test_convert():
    results = []

    # Fara cache
    t_nocache = run_and_time("./convert mat.in")
    results.append(f"Timp fără cache: {t_nocache:.4f} secunde")

    # Cu cache - diverse dimensiuni
    for size in [100, 1000, 10000]:
        t_cache = run_and_time(f"./convert mat.in --cache-size {size}")
        results.append(f"Timp cu cache {size} intrări: {t_cache:.4f} secunde")

    # Salvare rezultate
    with open("convert-testing.txt", "w") as f:
        f.write("Comparație performanță convertor Rust\n")
        f.write("--------------------------------------\n")
        f.write("\n".join(results))
        f.write("\n")

    print("[✔] Testele au fost rulate și salvate în convert-testing.txt")

if __name__ == "__main__":
    test_convert()
