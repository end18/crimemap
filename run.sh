#!/bin/bash
#루트로 실행시키세요.
uwsgi --http 0.0.0.0:8080 --wsgi-file crimemap.py --callable app --processes 4 --threads 2 --stats 0.0.0.0:8081


