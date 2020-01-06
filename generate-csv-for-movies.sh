#!/bin/bash
# Opens given file & parses it to produce the output with each film's position on each date
# If --years-only is provided then the title line only contains the year (first occurrence)
[ "$1" = "" ] && echo "ERROR: Need to provide input filename" && exit 1
for var in $@
do
  [ "$var" = "--years-only" ] && YEARS_ONLY=true && continue
  [ ! "$LIST_FILE" = "" ] && echo "ERROR: Cannot pass in two filenames" && exit 1
  [ ! -f $var ] && echo "ERROR: $var is not a valid file" && exit 1
  LIST_FILE=$var
done

FILMS_FILE=/tmp/films

# Get the film titles from the given file
GET_FILMS_SCRIPT_NAME=get-unique-film-titles.sh
GET_FILMS_SCRIPT=$(dirname ${BASH_SOURCE[0]})/$GET_FILMS_SCRIPT_NAME
[ ! -f $GET_FILMS_SCRIPT ] && echo "ERROR: Cannot find $GET_FILMS_SCRIPT_NAME script" && exit 1
$GET_FILMS_SCRIPT $LIST_FILE > $FILMS_FILE

# Generate the title line
if [ "$YEARS_ONLY" = "true" ]
then
  titles=$(cat $LIST_FILE | cut -d/ -f 1)
  titleLine=Title
  lastSetTitle=0
  for title in $titles
  do
    if [[ $title -eq $lastSetTitle ]]
    then
      currentTitle=
    else
      currentTitle=$title
      lastSetTitle=$title
    fi
    titleLine="$titleLine,$currentTitle"
  done
else
  titleLine="Title,$(cat $LIST_FILE | cut -d, -f 1 | sed 's/$/,/g' | xargs | sed 's/[[:space:]]//g')"
fi
echo $titleLine

char=","

[ -z $MAX_FILMS ] && MAX_FILMS=250

# Go through every film and print out it's position for each date
while IFS= read -r film
do
  echo -n "$film"
  highestPos=$((MAX_FILMS+1))
  while IFS= read -r fullLine
  do
    strippedLine=${fullLine%$film*}
    pos=$(awk -F"${char}" '{print NF-1}' <<< "${strippedLine}")
    [ $pos -lt $highestPos ] && highestPos=$pos
	[ $pos -gt $MAX_FILMS ] && [ $highestPos -gt $MAX_FILMS ] && pos=""
    echo -n ",$pos"
  done < "$LIST_FILE"
  echo
done < "$FILMS_FILE"
