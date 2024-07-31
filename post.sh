#!/usr/bin/env bash

# curl -v -X POST \
#   127.0.0.1:5000/extract-text \
#   -H 'Content-Type: multipart/form-data' \
#   -F 'image=@cousins_id.jpg'

curl -v -X POST \
  http://b0wc0g4.5.161.177.10.sslip.io/extract-text \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@cousins_id.jpg'
# curl -v localhost:5000/ping