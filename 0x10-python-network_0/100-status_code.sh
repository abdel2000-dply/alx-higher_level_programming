#!/bin/bash
# Only status code
curl -sI "$1" | awk '/HTTP\/1.1/ {print $2}'
