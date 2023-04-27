#!/bin/bash
#Takes in a URL, sends a request to that URL, and displays the size of the body of the response
#The size must be displayed in bytes
#curl must be used
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
