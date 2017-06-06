#!/bin/bash

for var in "$@"
do
    expand -t 4 $var > temp
    rm $var
    mv temp $var
done

