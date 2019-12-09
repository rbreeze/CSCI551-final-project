# adapted from Thomas Weise
# https://github.com/thomasWeise/distributedComputingExamples/blob/master/mpi/reducePrimes.c

from mpi4py import MPI
import sys
import numpy

if size<2:
  print("Need more than 1 process")
  quit()

DATA_SIZE = 1024

send = numpy.zeros(DATA_SIZE, dtype=int)
recv = numpy.zeros(DATA_SIZE, dtype=int)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if (rank == 0): 
  for i in range(DATA_SIZE, 0, -1): 
    send[i] = (i + 1)

count = (DATA_SIZE / size)
comm.scatter(send, recv, count, root=0)

res = count
for i in range(count, 0, -1):  
  for in range(int(sqrt(recv[i]))|1, 1, -2): 
    if ((recv[i] % j) == 0):
      res -= 1
      break 

print("Process " + rank + " discovered " + res + " primes in the numbers from " + recv[0] + " to " + recv[count-1] + ".")

comm.Reduce(res, recv, op=MPI_SUM, root=0)

if(rank == 0): 
  printf("The total number of primes in the first " + count*size + " natural numbers is " + recv[0] + ".")