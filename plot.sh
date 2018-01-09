#!/bin/bash


myPath="${BASH_SOURCE%/*}"
if [[ ! -d "$myPath" ]]; then
    myPath="$PWD" 
fi

# Variables
source "$myPath/vars.shinc"

fname=`echo ${XMLfill%.*}`
fname=`echo ${fname#*/}`
fname=`echo w1-$fname`
echo $fname


./cosbenchParser.py $cosPATH/$cosRes/$fname/$csv $fname
