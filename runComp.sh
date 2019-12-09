printf "python,$($2),"
mpirun -f hosts python3 $1/$1.py $2 | grep "Elapsed" | awk '{print $2}' >> results/$1.csv
printf "c,,$($2),"
mpirun -f hosts ./$1/$1 $2 | grep "Elapsed" | awk '{print $2}' >> results/$1.csv