#!/bin/bash

python ./deduct.py

outz=$(cat deducted)

echo $outz

if [ "$outz" -gt 10 ]
then
    echo "Pos"
    echo $outz	
fi

rm -f deducted
