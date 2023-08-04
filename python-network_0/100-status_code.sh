#!/bin/bash
#sends a request to a URL passed as an argument
curl -sLw "%{http_code}" -o /dev/null "$1"
