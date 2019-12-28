#!/bin/bash
FILE=snapshot-urls.txt

urls="$(cat $FILE)"
for url in $urls
do
  full=$(echo $url | cut -d/ -f 5-7 )
  year=$(echo $full | cut -d/ -f 1)
  month=$(printf "%02d" $(echo $full | cut -d/ -f 2))
  day=$(printf "%02d" $(echo $full | cut -d/ -f 3))
  date="${year}-${month}-${day}"
  command="python3 gen-csv.py $url"
  output=$(eval $command)
  echo "$full,$output"
done
