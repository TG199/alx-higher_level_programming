#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -lt 1 ]; then
	echo "Usage: $0 URL" >&2
	exit 1
fi

URL=$1
curl -sI "$URL" | grep "Content-Length:" | cut -d " " -f 2;
