iterations=$2
sizes=$3

for i in $(seq 1 $sizes)
do
  for j in $(seq 0 $iterations)
  do
    ./comp.sh $1 $((10**$i))
  done
done