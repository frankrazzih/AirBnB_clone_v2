#!/usr/bin/python3
"""create an archive using fabric"""
from fabric.api import local
from datetime import datetime
def do_pack():
    now = datetime.now()
    date = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + date + ".tgz"
    if (local("tar -czvf" + filename + "/data/webstatic/*")):
        local("mkdir /data/web_static/versions")
        local("mv /data/web_static/*.tgz data/web_static/versions")
        return filename
    else:
        return None