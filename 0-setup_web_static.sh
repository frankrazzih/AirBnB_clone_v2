#!/usr/bin/env bash
#set up server for deployment
#check if nginx exists
if ! command -v nginx > tmpfile; then
	sudo apt update
	sudo apt install nginx
fi

if [[ ! -d /data ]];then
	sudo mkdir /data
fi
sudo chown -R ubuntu:ubuntu /data
if [[ ! -d /data/web_static/releases/test/ ]]; then
	sudo mkdir -p /data/web_static/releases/test/
fi

if [[ ! -d /data/web_static/shared/ ]]; then
	sudo mkdir /data/web_static/shared/
fi

echo 'nginx configuration okay' | sudo tee /data/web_static/releases/test/index.html

if [[ -L /data/web_static/current ]]; then
	sudo rm /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test /data/web_static/current
text="location /hbnb_static {alias /data/web_static/current/;}"
sudo sed -i "/server/a\\$text\nq" /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0