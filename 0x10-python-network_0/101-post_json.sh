#!/bin/bash
# cURL a JSON fil
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
