#!/bin/bash
# Opens given file & parses it to produce the output with each film's position on each date
[ "$1" = "" ] && echo "ERROR: Need to provide input filename" && exit 1
[ ! -f $1 ] && echo "ERROR: $1 is not a valid file" && exit 1

LIST_FILE=$1
FILMS_FILE=/tmp/films

# Get the film titles from the given file
GET_FILMS_SCRIPT_NAME=get-unique-film-titles.sh
GET_FILMS_SCRIPT=$(dirname ${BASH_SOURCE[0]})/$GET_FILMS_SCRIPT_NAME
[ ! -f $GET_FILMS_SCRIPT ] && echo "ERROR: Cannot find $GET_FILMS_SCRIPT_NAME script" && exit 1
$GET_FILMS_SCRIPT $LIST_FILE > $FILMS_FILE

# Generate the title line
titleLine="Title,$(cat $LIST_FILE | cut -d, -f 1 | sed 's/$/,/g' | xargs | sed 's/[[:space:]]//g')"
echo $titleLine

char=","

# Go through every film and print out it's position for each date
while IFS= read -r film
do
  echo -n "$film"
  while IFS= read -r fullLine
  do
    strippedLine=${fullLine%$film*}
    pos=$(awk -F"${char}" '{print NF-1}' <<< "${strippedLine}")
    echo -n ",$pos"
  done < "$LIST_FILE"
  echo
done < "$FILMS_FILE"
