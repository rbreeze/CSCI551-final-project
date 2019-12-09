pi: pi/pi.o
	mpicc pi/pi.c -o pi/pi

avg: avg/avg.o
	mpicc avg/avc.c -o avg/avg

primes: primes/primes.o
	mpicc primes/primes.c -o primes/primes