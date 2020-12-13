#!/bin/bash
for folder in $(find . -wholename './.*' -prune -o -type d -print | sort | sed '1d')
do  
	day="${folder:2:5}" # remove trailing backslash
	cd "$day"
	echo -e "----- DAY $day ----- ($(pwd))"
	python3 "${day}.py"
	cd ../
done
