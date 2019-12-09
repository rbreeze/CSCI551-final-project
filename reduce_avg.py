# adapted from mpitutorial.com C program by Wes Kendall

from mpi4py import MPI
from random import seed
from random import random
import sys

seed(1)

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if size<2:
  print("Need more than 1 process")
  quit()

def create_rand_nums(num_elements): 
  rand_nums = []
  for i in range(num_elements):
    rand_nums.append(randint(0, RAND_MAX))
  return rand_nums

if (sys.argc != 2): 
  print("Usage: avg num_elements_per_proc\n")

num_elements_per_proc = atoi(sys.argv[1])

rand_nums = create_rand_nums(num_elements_per_proc)

local_sum = 0
i = 0
for i in range(num_elements_per_proc): 
  local_sum += rand_nums[i]

print("Local sum for process " + str(rank) + " - " + str(local_sum) + ", avg = " + str(local_sum / num_elements_per_proc))

global_sum = 0;
comm.Reduce(local_sum, global_sum, op=MPI.SUM, root=0)

if (rank == 0): 
  print("Total sum = " + global_sum + ", avg = " + global_sum / (world_size * num_elements_per_proc))

