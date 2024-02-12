#!/usr/bin/python3
"""create an archive using fabric"""
from fabric import Connection
from datetime import datetime

"""def do_pack: create an archive in the localhost"""


def do_pack():
    local = Connection('localhost')
    now = datetime.now()
    date = now.strftime("%Y-%m-%d-%H:%M:%S")
    filename = "web_static_" + date + ".tgz"
    if (local.run("tar -czvf" + filename + "/webstatic/*")):
        local.run("mkdir /web_static/versions")
        local.run("mv /web_static/*.tgz /web_static/versions")
        return filename
    else:
        return None
