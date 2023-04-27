#!/bin/bash
# Gets the size of the body of a response from a URL and curl must be used
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
