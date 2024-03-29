# adapted from Thomas Weise
# https://github.com/thomasWeise/distributedComputingExamples/blob/master/mpi/reducePrimes.c

from mpi4py import MPI
import sys
import numpy
import math
from time import process_time 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if size<2:
  print("Need more than 1 process")
  quit()

DATA_SIZE = int(sys.argv[1])

nums = numpy.zeros(DATA_SIZE, dtype=int)

comm.Barrier()
t1_start = process_time() 

if (rank == 0): 
  for i in range(DATA_SIZE-1, 0, -1): 
    nums[i] = (i + 1)
  send = [[] for _ in range(size)]
  for i, chunk in enumerate(nums):
    send[i % size].append(chunk)
else:
  recv = None
  send = None

recv = comm.scatter(send, root=0)
count = int(DATA_SIZE / size)

res = 0; # here: count how many prime numbers are contained in the array
low = recv[0]; 
high = recv[count-1]
if (low % 2 == 0):
  low += 1

for i in range(low, high, 2):
  flag = 0

  for j in range(2, int(i/2)):
    if (i % j == 0):
      flag = 1
      break

  if (flag == 0): 
    res += 1

t1_stop = process_time() 

print("Process " + str(rank) + " discovered " + str(res) + " primes in the numbers from " + str(recv[0]) + " to " + str(recv[count-1]) + ".")

res = numpy.sum(numpy.array(res)).astype('int')

total = numpy.zeros(1, dtype='float64')

comm.Reduce(res, total, op=MPI.SUM, root=0)

comm.Barrier()
t1_stop = process_time() 

if(rank == 0): 
  print("The total number of primes in the first " + str(count*size) + " natural numbers is " + str(total) + ".")
  print("Elapsed Time: " + str(t1_stop-t1_start))
