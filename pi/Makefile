CC=mpicc

pi/pi.o: 
	$(MPICC) -c pi/pi.c -lm 

pi/pi: pi/pi.o
	$(MPICC) pi/pi.o -o pi/pi

avg/avg: avg/avg.o
	$(MPICC) avg/avc.o -o avg/avg

avg/avg.o: 
	$(MPICC) -c avg/avg.c -lm 

primes/primes: primes/primes.o
	$(MPICC) primes/primes.o -o primes/primes

primes/primes.o: 
	$(MPICC) -c primes/primes.c -lm 