read arr
read arr1
tot=0
for i in ${arr1[@]}; do
  let tot+=$i
done
echo "$tot"