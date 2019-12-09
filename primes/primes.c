// Source: https://github.com/thomasWeise/distributedComputingExamples/blob/master/mpi/reducePrimes.c
#include <mpi.h>    // import MPI header
#include <stdio.h>  // needed for printf
#include <stdlib.h>
#include <math.h>   // needed for sqrt

int main(int argc, char *argv[]) {

  if (argc != 2) {
      fprintf(stderr, "Usage: primes max\n");
      exit(1);
  }

  int DATA_SIZE = atoi(argv[1]);

  int send[DATA_SIZE], recv[DATA_SIZE];
  int rank, size, count, root, res, i, j;
  MPI_Status status;

  MPI_Init(&argc, &argv); // initialize MPI
  MPI_Comm_rank(MPI_COMM_WORLD, &rank); // get own rank/ID
  MPI_Comm_size(MPI_COMM_WORLD, &size); // get total number of processes

  if (rank == 0) { //generate data (i.e., the first DATA_SIZE natural numbers) if root
    for(i = 0; i < DATA_SIZE; i++) { send[i] = i + 1; }
  }

  double start = MPI_Wtime();

  count = (DATA_SIZE / size); // divide the data among _all_ processes
  // scatter: if rank=0, send data (and get own share); otherwise: receive data
  MPI_Scatter(send, count, MPI_INT, recv, count, MPI_INT, 0, MPI_COMM_WORLD);

  // each node now processes its share of the numbers
  res = 0; //here: count how many prime numbers are contained in the array
  for(i = 0; i < count; i++) { // for each index in the array
    int num = recv[i];
    int prime = 0; 
    if (num > 1) { 
      for (j = 2; j < sqrt(num); j++) { // check factors
        if (num % j == 0) { // if a number can be divided by j
          break; 
        } else {
          prime = 1;
        }
      }
    }
    if (prime) {
      printf("%d\n", num); 
      res++;
    }
  }

  printf("Process %d discovered %d primes in the numbers from %d to %d.\n", rank, res, recv[0], recv[count-1]);

  // reduce: each node takes results, applies operator MPI_SUM locally, sends result to root, where MPI_SUM is
  // applied again. (here: locally summing up does not matter, as only 1 number). The final result is returned.
  MPI_Reduce(&res, recv, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  if(rank == 0) { //if root, print
    printf("Primes in the first %d natural numbers is %d.\n", (count*size), recv[0]);
  }

  MPI_Barrier(MPI_COMM_WORLD);
  double end = MPI_Wtime();

  double duration = end-start;
  double global;

  MPI_Reduce(&duration,&global,1,MPI_DOUBLE,MPI_MAX,0,MPI_COMM_WORLD);
  if(rank == 0) {
    printf("Elapsed Time: %f\n",global);
  }

  MPI_Finalize(); // shut down MPI

  return 0;
}