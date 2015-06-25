#!/bin/bash

echo "Cleaning..."

rm -r -f ./package/*

echo "Generating PKGBUILD..."

python archpack_generator.py $1 $2
