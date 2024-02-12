#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    local = Connection('localhost')
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + dt + ".tgz"
    dir = "versions"
    if (path.isdir(dir)):
        pass
    else:
        local.run("mkdir /versions")
    result = local.run("tar -czvf " + filename + "/webstatic/*")
    if (result.exited == 0):
        local.run("mv /web_static/*.tgz /versions")
        return filename
    else:
        None
