#!/bin/bash
# script that displays the size of the body of the response
curl -s -X GET "$1" | wc -c
