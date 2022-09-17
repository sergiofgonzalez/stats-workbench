#!/bin/bash

curl -v -X POST \
  --header "Content-Type: application/json" \
  --data '{"title":"Watch T.V."}' \
  http://localhost:5000/todo/api/v1/tasks

