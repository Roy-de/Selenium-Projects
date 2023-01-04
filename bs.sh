#! /usr/bin/bash
regex='(^\(\d{3}\) \d{3}\-\d{4}$)|(^\d{3}\-\d{3}\-\d{4}$)'
file='input.txt'
if [[ $file =~ $regex ]]; then
echo "Done"
echo ${BASH_REMATCH[1]}
fi