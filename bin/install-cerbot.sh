#!/usr/bin/env bash

add-apt-repository ppa:certbot/certbot
apt update
apt install python-certbot-nginx
certbot --nginx -d www.evengram.xyz
certbot --nginx -d api.evengram.xyz