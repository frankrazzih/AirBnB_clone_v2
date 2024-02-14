#!/usr/bin/python3
# full deployment
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


def deploy():
    """Create and distribute an archive to a web server."""
    archive_path = do_pack()
    result = do_deploy(archive_path)
    return result
