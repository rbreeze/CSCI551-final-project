"""
Source: https://github.com/erdc/mpi4py/blob/master/demo/compute-pi/cpi-cco.py

Parallel PI computation using Collective Communication Operations (CCO)
within Python objects exposing memory buffers (requires NumPy).
usage::
  $ mpiexec -n <nprocs> python cpi-buf.py
"""

from mpi4py import MPI
from math   import pi as PI
from numpy  import array
import sys
from time import process_time 

def comp_pi(n, myrank=0, nprocs=1):
    h = 1.0 / n
    s = 0.0
    for i in range(myrank + 1, n + 1, nprocs):
        x = h * (i - 0.5)
        s += 4.0 / (1.0 + x**2)
    return s * h

def prn_pi(pi, PI):
    message = "PI=%.16f"
    print  (message % (pi))

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

n    = array(0, dtype=int)
pi   = array(0, dtype=float)
mypi = array(0, dtype=float)

if myrank == 0:
    _n = sys.argv[1]
    n.fill(_n)

comm.Barrier()
t1_start = process_time() 

comm.Bcast([n, MPI.INT], root=0)
if n == 0:
    break
_mypi = comp_pi(n, myrank, nprocs)
mypi.fill(_mypi)
comm.Reduce([mypi, MPI.DOUBLE], [pi, MPI.DOUBLE],
            op=MPI.SUM, root=0)

comm.Barrier()
t1_stop = process_time() 

if myrank == 0:
    prn_pi(pi, PI)
    print("Elapsed Time: " + str(t1_stop-t1_start))