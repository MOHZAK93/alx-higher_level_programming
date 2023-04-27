#!/bin/bash
# Deletes a request to a URL passed as the first argument
curl -siLk -X OPTIONS "$1" | grep -oiE 'Allow: .+' | cut -d ' ' -f2-
