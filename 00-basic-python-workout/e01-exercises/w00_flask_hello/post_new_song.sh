#!/bin/bash
curl -v -X POST \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "artist='R.E.M.'" \
  --data-urlencode "title='Driver 8'" \
  --data-urlencode "rating=5" \
  http://localhost:5000/api/songs