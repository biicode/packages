#!/bin/bash

echo "Cleaning..."

rm -r -f ./package/*

echo "Generating PKGBUILD..."

python archpack_generator.py $1 $2

echo "Generating AUR package..."

./make.sh

echo "Uploading package to AUR..."

aurploader ./package/*.src.tar.gz --login ./aur_login --auto --keep-cookiejar
