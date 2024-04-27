#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
        exit 1
	fi

# URL provided as argument
	URL=$1

# Send request using curl and get the size of the response body in bytes
	SIZE=$(curl -s -w '%{size_download}' -o /dev/null "$URL")

# Display the size of the response body
	echo "Size of the response body: $SIZE bytes"

