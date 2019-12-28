#!/bin/bash
# Generates the FULL CSV using all the URLs in $FILE
FILE=trimmed-urls.txt

urls="$(cat $FILE)"
for url in $urls
do
  full=$(echo $url | cut -d/ -f 5-7 )
  command="python3 gen-csv.py $url"
  output=$(eval $command)
  echo "$full,$output"
done
