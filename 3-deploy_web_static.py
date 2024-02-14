#!/usr/bin/python3
# full deployment
from os import path
from fabric.operations import env
from fabric.operations import run
from fabric.operations import local
from datetime import datetime


def do_deploy(archive_path):
    """deploys an archive to a remote server"""

    web01 = "ubuntu@54.221.181.151"
    web02 = "ubuntu@100.26.169.188"
    env.hosts = [web01, web02]

    if not path.isfile(archive_path):
        return False
    ls = archive_path.split('/')
    file_name = ls[-1]
    uncomp_file = file_name.split('.')
    uncomp_file = uncomp_file[0]
    # on the localhost
    result1 = local("scp -o 'StrictHostKeyChecking=no' {} {}:/tmp/".format(archive_path, web01))
    result2 = local("scp -o 'StrictHostKeyChecking=no' {} {}:/tmp/".format(archive_path, web02))
    if (result1.failed or result2.failed):
        return False
    # on the servers
    # uncompress
    result1 = run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(file_name, uncomp_file))
    # remove archive and symlinks
    result2 = run("rm /tmp/{} && rm /data/web_static/current".format(file_name))
    # create symlink
    result3 = run("ln -s /data/web_static/releases/{} /data/web_static/current".format(uncomp_file))
    if (result2.failed or result1.failed or result3.failed):
        return False
    else:
        return True

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.now()
    dt = now.strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + dt + ".tgz"
    dir = "versions"
    if (path.isdir(dir)):
        pass
    else:
        local("mkdir versions")
    result = local("tar -czvf {} webstatic".format(filename))
    if (result.exited == 0):
        local("mv *.tgz versions")
        return filename
    else:
        None

def deploy():
    """Create and distribute an archive to a web server."""
    archive_path = do_pack()
    result = do_deploy(archive_path)
    return result
