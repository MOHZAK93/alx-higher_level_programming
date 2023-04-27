#!/bin/bash
# Deletes a request to a URL passed as the first argument
curl -s -X DELETE "$1"
