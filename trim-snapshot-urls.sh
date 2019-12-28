#!/bin/bash
# Goes through $FILE & only prints out 1 URL per month
FILE=snapshot-urls.txt

prevYear="undefined"
prevMonth="undefined"
urls="$(cat $FILE)"
for url in $urls
do
  full=$(echo $url | cut -d/ -f 5-7 )
  year=$(echo $full | cut -d/ -f 1)
  month=$(printf "%02d" $(echo $full | cut -d/ -f 2))
  if [ "$year" = "$prevYear" ] && [ "$month" = "$prevMonth" ]
  then
    continue
  fi
  echo $url
  prevYear=$year
  prevMonth=$month
done
