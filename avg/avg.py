# adapted from mpitutorial.com C program by Wes Kendall

from mpi4py import MPI
from random import seed
from random import randint
import numpy
import sys
from time import process_time 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if size<2:
  print("Need more than 1 process")
  quit()

def create_rand_nums(num_elements): 
  rand_nums = []
  for i in range(num_elements):
    rand_nums.append(randint(0, 100))
  return rand_nums

if (len(sys.argv) != 2): 
  print("Usage: avg num_elements\n")

num_elements_per_proc = int( int(sys.argv[1]) / size)

rand_nums = create_rand_nums(num_elements_per_proc)

local_sum = 0
global_sum = numpy.zeros(1, dtype='float64')

i = 0

comm.Barrier()
t1_start = process_time() 

for i in range(num_elements_per_proc): 
  local_sum += rand_nums[i]

print("Local sum for process " + str(rank) + " - " + str(local_sum) + ", avg = " + str(local_sum / num_elements_per_proc))

local_sum = numpy.sum(numpy.array(local_sum)).astype('float64')

comm.Reduce(local_sum, global_sum, op=MPI.SUM, root=0)

comm.Barrier()
t1_stop = process_time() 

if (rank == 0): 
  print("Total sum = " + str(global_sum) + ", avg = " + str(global_sum / (size * num_elements_per_proc)))
  print("Elapsed Time: " + str(t1_stop-t1_start))
