iterations=$2
sizes=$3

for i in {0..$iterations}
do
  for j in {1..$sizes}
  do
    ./comp.sh $1 $((10**$j))
  done
done