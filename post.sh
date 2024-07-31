#!/usr/bin/env bash

curl -v -X POST \
  127.0.0.1:5000/extract-text \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@cousins_id.jpg'

# curl -v localhost:5000/ping