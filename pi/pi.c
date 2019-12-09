// Source: https://www.mcs.anl.gov/research/projects/mpi/tutorial/mpiexmpl/src/pi/C/main.html

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char* argv[]) {

  if (argc != 2) {
      fprintf(stderr, "Usage: pi num_iterations\n");
      exit(1);
  }
  int n = atoi(argv[1]);

  int done = 0, myid, numprocs, i;
  double mypi, pi, h, sum, x;

  MPI_Init(&argc,&argv);
  MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
  MPI_Comm_rank(MPI_COMM_WORLD,&myid);

  MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

  MPI_Barrier(MPI_COMM_WORLD);
  double begin = MPI_Wtime();
  
  h   = 1.0 / (double) n;
  sum = 0.0;
  for (i = myid + 1; i <= n; i += numprocs) {
      x = h * ((double)i - 0.5);
      sum += 4.0 / (1.0 + x*x);
  }
  mypi = h * sum;
    
  MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0,
       MPI_COMM_WORLD);

  MPI_Barrier(MPI_COMM_WORLD);
  double end = MPI_Wtime();
    
  if (myid == 0) {
    printf("PI=%.16f\n", pi);
    printf("Elapsed Time: %f\n",  end-begin);
  }

  MPI_Finalize();

  return 0;

}
