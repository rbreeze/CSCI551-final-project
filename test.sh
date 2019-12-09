iterations=$2
sizes=$3

for i in {0..$iterations}
do
  for j in {1..$sizes}
  do
    cursize=$((10 ** $j))
    ./comp.sh $1 $cursize
  done
done