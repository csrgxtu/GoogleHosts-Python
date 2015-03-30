import multiprocessing


workers = []

def worker(num):
  """worker function"""
  print "Worker:", num
  workers.append(num)
  return

if __name__ == '__main__':
  jobs = []
  for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,)) 
    jobs.append(p)
    p.start()
  
  for j in jobs:
    j.join()

  print workers
