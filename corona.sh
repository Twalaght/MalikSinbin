curl -s https://corona-stats.online | grep "Australia" |
	sed "s/\s*//g ; s/║//g ; s/│/;/g" |
	awk -F';' '{print "Cases " $3 " (" $4") Deaths " $5 " (" $6")"}'
