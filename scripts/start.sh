#!/bin/bash

gunicorn \
  --chdir /usr/src/app/rest-gateway/src \
  --worker-class gevent \
  --workers 1 \
  --bind "0.0.0.0:$FLASK_RUN_PORT" \
  wsgi:app \
  --max-requests 10000 \
  --timeout 5 \
  --keep-alive 5 \
  --log-level info
