CC=mpicc

pi/pi: pi/pi.o
	$(CC) pi/pi.o -o pi/pi

pi/pi.o: 
	$(CC) -c pi/pi.c -lm 

avg/avg: avg/avg.o
	$(CC) avg/avc.o -o avg/avg

avg/avg.o: 
	$(CC) -c avg/avg.c -lm 

primes/primes: primes/primes.o
	$(CC) primes/primes.o -o primes/primes

primes/primes.o: 
	$(CC) -c primes/primes.c -lm 