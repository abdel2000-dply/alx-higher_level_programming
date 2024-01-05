#!/bin/bash
# Only status code
curl -sI $1 | grep HTTP/1.1 | awk '{print $2}'
