#!/bin/bash

# $ ./ping_server.sh                                                 
# waiting for ServerXY ....................
# Server is back online


printf "%s" "waiting for ServerXY ..."
while ! ping -c 1 -n -w 1 147.153.237.192 &> /dev/null
do
    printf "%c" "."
done
printf "\n%s\n"  "Server is back online"
