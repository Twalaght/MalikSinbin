#!/bin/bash
print_center(){
	local x
	local y
	text="$*"
	x=$(( ($(tput cols) - ${#text}) / 2))
	echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
	echo -ne "\033[${y};${x}f$*"
}

# clear the screen, put the cursor at line 10, and set the text color
# to light blue.
echo -ne "\\033[2J\033[10;1f\e[94m"

# do it!
print_center 'Matt be with you, brother'
sleep 2
