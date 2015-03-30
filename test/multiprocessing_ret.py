import multiprocessing as mp
import random
import string

# Define an output queue
output = mp.Queue()

def worker(num):
  output.put(num ** 2)

# Setup a list of processes that we want to run
processes = [mp.Process(target=worker, args=(x,)) for x in range(4)]

# Run processes
for p in processes:
  p.start()

# Exit the completed processes
for p in processes:
  p.join()

# Get process results from the output queue
results = [output.get() for p in processes]
print results
