#!/bin/bash
# Opens arg1 and prints out all the unique film titles
[ "$1" = "" ] && echo "ERROR: Need to provide input filename" && exit 1
[ ! -f $1 ] && echo "ERROR: $1 is not a valid file" && exit 1

# First sed replaces , with a new line
# Second sed removes blank lines
# Third sed removes the dates so we only have the movie names
cat $1 | sed 's/,/\
/g' | sed '/^$/d' | sort -u | sed '/^[[:digit:]][[:digit:]][[:digit:]][[:digit:]]\/[[:digit:]]/d'
