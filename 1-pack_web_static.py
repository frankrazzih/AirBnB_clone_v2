#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from os import path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + dt + ".tgz"
    dir = "versions"
    if (path.isdir(dir)):
        pass
    else:
        local("mkdir /versions")
    result = local("tar -czvf " + filename + "/webstatic/*")
    if (result.exited == 0):
        local("mv /web_static/*.tgz /versions")
        return filename
    else:
        None
