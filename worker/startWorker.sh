#!/bin/bash
cd celery
python3 -m celery -A tasks worker -l info -n worker$1@%h