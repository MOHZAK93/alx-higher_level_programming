#!/bin/bash
#Sends a GET request and displays body of the response
curl -sLX POST -d 'email=test@gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
