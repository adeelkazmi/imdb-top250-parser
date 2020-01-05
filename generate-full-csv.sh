#!/bin/bash
# Opens arg1 and generates the FULL CSV using all the URLS in that file
if [ "$1" = "" ]
then
  FILE=trimmed-urls.txt
  echo "No input file provided, using \"$FILE\" for the URLs"
else
  FILE=$1
fi

[ ! -f $FILE ] && echo "ERROR: $1 is not a valid file" && exit 1

urls="$(cat $FILE)"
for url in $urls
do
  full=$(echo $url | cut -d/ -f 5-7 )
  command="python3 gen-csv.py $url"
  output=$(eval $command)
  echo "$full,$output"
done
