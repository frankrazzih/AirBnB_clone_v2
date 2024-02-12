#!/usr/bin/python3
# create an archive using fabric
from fabric import Connection
from datetime import datetime
from os import path


def do_pack():
    """create an archive in the localhost."""
    local = Connection('localhost')
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + dt + ".tgz"
    if (path.isdir(versions)):
        pass
    else:
        local.run("mkdir /versions")
    result = local.run("tar -czvf " + filename + "/webstatic/*")
    if (result.exited == 0):
        local.run("mv /web_static/*.tgz /versions")
        return filename
    else:
        None
    
