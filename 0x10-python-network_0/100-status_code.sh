#!/bin/bash
#Only status code
curl -sw '%{http_code}' -o /dev/null "$1"01~
