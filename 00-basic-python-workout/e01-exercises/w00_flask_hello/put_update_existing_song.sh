#!/bin/bash
curl -v -X PUT \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "artist='Updated artist'" \
  --data-urlencode "title='Updated title'" \
  --data-urlencode "rating=1" \
  http://localhost:5000/api/songs/1