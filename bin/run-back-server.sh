#!/bin/bash

#docker exec  -it ifn_web_1 python3.7 manage.py runserver 0:8000
case "$(uname -s)" in
    Darwin)
    echo 'Mac OS X'
    docker exec  -it app_web_inaturalist python3.7 manage.py runserver 0:8000
    ;;
    Linux)
    echo 'Linux'
    docker exec  -it app_web_inaturalist python3.7 manage.py runserver 0:8000
    ;;
    CYWGWIN*|MINGW32*|MSYS*|MINGW*)
    echo 'Windows'
    winpty docker exec  -it app_web_inaturalist python3.7 manage.py runserver 0:8000
    ;;
esac