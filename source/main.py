import time


# Count the number of basic operations in 1 second
start_time = time.time()
count = 0

while time.time() - start_time < 1:
    count += 1

print(f"Number of basic operations in 1 second: ", count)
