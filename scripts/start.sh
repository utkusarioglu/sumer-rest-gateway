#!/bin/bash

gunicorn \
  --chdir /usr/src/app/rest-gateway/src \
  --worker-class gevent \
  --workers 4 \
  --bind 0.0.0.0:80 \
  wsgi:app \
  --max-requests 10000 \
  --timeout 5 \
  --keep-alive 5 \
  --log-level info
