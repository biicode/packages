#!/bin/bash

mkaurball -f
rm -f ./*.pkg.tar.xz ./*.deb
mkdir package
mv ./*.tar.gz package
