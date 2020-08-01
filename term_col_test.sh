#!/bin/bash
 
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
 
for color in {0..16} ; do #Colors
	#Display the color
	echo -en "\e[38;5;${color}m ${color}"
done
echo #New line
 
exit 0

# 10 = Green, 12 = blue, 15 = whiteish
