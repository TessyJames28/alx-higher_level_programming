#!/bin/bash
# script that sends a jason POST request
curl -sH "Content-Type: application/json" -d "$(cat $2)" $1
