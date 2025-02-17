import time

start = time.time()
print("Stopwatch started! Press Ctrl+C to stop.")

try:
    while True:
        elapsed = round(time.time() - start, 2)
        print(f"\rElapsed time: {elapsed} seconds", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\nFinal time: {elapsed} seconds")
    print("Stopwatch stopped!")
