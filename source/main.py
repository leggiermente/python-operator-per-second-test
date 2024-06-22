from time import time


# Count the number of basic operations in 1 second
try:
    start = time()
    counter = 0
    while counter < 10000000:
        counter += 1
finally:
    end = time()
    print("Number of basic operations in 1 second: ", counter/(end-start))
