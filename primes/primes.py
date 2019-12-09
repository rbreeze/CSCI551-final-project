# Source: https://stackoverflow.com/questions/55112272/applying-reduce-and-broadcast-in-mpi

import numpy as np
import platform
import sys
from mpi4py import MPI
import math
from time import process_time 

comm = MPI.COMM_WORLD
id = comm.Get_rank()
p = comm.Get_size()

# Find the primes between 2 and k. Initialize k.
k=int(math.sqrt(int(sys.argv[1])))
# Define a list S_k of the primes between 2 and k
S_k=[]
# Define a list to store numbers that aren't prime between 2 and k.
not_prime = []
# Define a list S_k2 of the primes between k and k**2
S_k2=[]


# Count the number of primes from 2 to k
for i in range(2, k+1):
    if i not in not_prime:
        S_k.append(i)
        for j in range(i*i, k+1, i):
            not_prime.append(j)

comm.Barrier()
t1_start = process_time() 

# Find the number of primes between k and k**2 by
# pararllelizing the n-loop.
b=(k**2-k)/p
for n in range(int(k+(id)*b),int(k+(id+1)*b)):
    counter = 0
    for i in range(len(S_k)):
        if (n % S_k[i]) == 0:
            break
        else:
            counter = counter + 1
    if (counter==len(S_k)):
        S_k2.append(n)

# Compute the amount of primes in the two lists.
processor_num_primes = len(S_k2)
original_num_primes = len(S_k)

# Broadcast the amount of primes and calculate the unions
# of sets of integers.
countb = 0
totalb = 0
for i in range(0,p):
    countb = comm.bcast(S_k2,i)
    totalb = totalb + len(countb)
total = comm.reduce(totalb,MPI.BOR,0)

comm.Barrier()
t1_stop = process_time() 

if (id == 0):
    print("Primes found between",2,"and",k*k,"is:",total+original_num_primes)
    print("Elapsed Time: " + str(t1_stop-t1_start))