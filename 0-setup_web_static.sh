#!/usr/bin/env bash
#set up server for deployment
#check if nginx exists
if [[ ! which nginx ]]; then
	sudo apt update
	sudo apt install nginx
fi

if [[ ! -d /data/web_static/releases/test ]]; then
	sudo mkdir -p /data/web_static/releases/test
fi

if [[ ! -d /data/web_static/shared ]]; then
	sudo mkdir /data/web_static/shared
fi

sudo echo 'nginx configuration okay' > /data/web_static/releases/test/index.html

if [[ -L /data/web_static/current ]]; then
	sudo rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:group /data/
text="location /data/web_static/current/ {
	alias hbnb_static;
}"
sudo sed -i "/server/a\\$text\q" /etc/nginx/nginx.conf
sudo service nginx restart
