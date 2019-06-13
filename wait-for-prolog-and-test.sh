#!/bin/bash

echo "Waiting prolog on 8000..."

while ! nc -z prolog 8000; do
  sleep 0.1
done

echo "Prolog is ready, start test"
mutmut run

