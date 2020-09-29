#!/bin/bash
cd /c/Users/tosha/Custom_tmp
while True 
	do
	sleep 10
	find -maxdepth 1 -type d | wc -l
	find -maxdepth 1 -type f | wc -l
done