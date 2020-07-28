#!/bin/bash

# Store the name of the above folder, the comic name
name=${PWD##*/}

# Sanitize all spaces
name=${name// /_}

# Zip all files in the directory and store it in tmp
zip -r -j /tmp/"$name".zip .

# Sync the comic to the phone over ssh
rsync -av -e "ssh -p 2222" "/tmp/$name.zip" twi@"$PHONE_IP":SDCard/Comics/
