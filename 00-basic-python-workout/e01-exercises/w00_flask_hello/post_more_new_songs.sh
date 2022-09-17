#!/bin/bash

curl -v -X POST \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "artist='Daft Punk'" \
  --data-urlencode "title='Get lucky'" \
  --data-urlencode "rating=5" \
  http://localhost:5000/api/songs

curl -v -X POST \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "artist='Danny Elfman'" \
  --data-urlencode "title='The Simpsons Intro Theme'" \
  --data-urlencode "rating=4" \
  http://localhost:5000/api/songs