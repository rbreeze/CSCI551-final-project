CC=mpicc

pi/pi:
	$(CC) pi/pi.c -o pi/pi -lm

avg/avg:
	$(CC) avg/avg.c -o avg/avg -lm

primes/primes:
	$(CC) primes/primes.c -o primes/primes -lm