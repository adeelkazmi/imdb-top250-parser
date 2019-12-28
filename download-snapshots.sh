#!/bin/bash
FILE=../snapshot-urls.txt

urls="$(cat $FILE)"
for url in $urls
do
  full=$(echo $url | cut -d/ -f 5-7 )
  year=$(echo $full | cut -d/ -f 1)
  month=$(printf "%02d" $(echo $full | cut -d/ -f 2))
  day=$(printf "%02d" $(echo $full | cut -d/ -f 3))
  filename="${year}-${month}-${day}.xml"
  command="curl $url -o $filename &> /dev/null"
  echo $command
  eval $command
done
