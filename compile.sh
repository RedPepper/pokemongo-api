#!/bin/bash

rm -rf pogo/proto
cd ./proto/
./compile_single.py -l python -o ../
cd ../
