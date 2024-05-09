#!/bin/bash

if [ $# -lt 1 ]; then
	echo "Usage: $0 URL" >&2
	exit 1
fi

URL=$1
sz="%{size_download}\n"

curl -s -o /dev/null -w "$sz" "$URL";
