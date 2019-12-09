CC=mpicc

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

pi/pi: pi/pi.o
	$(CC) -o pi/pi pi/pi.o