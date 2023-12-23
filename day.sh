#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo "Usage : $0 day_number"
    exit 1
fi

day=$(printf %02d $1)

cp -a 00 $day
# mv $day/day00a.py $day/day${day}a.py
# mv $day/day00b.py $day/day${day}b.py