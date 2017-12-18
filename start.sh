#!/bin/bash
for i in `seq 1 100`;
do
	python3 dhlattack.py &
done
wait