#!/usr/bin/python3
# full deployment
from 1-pack_web_static import do_pack
"""create a compressed archive"""
from 2-do_deploy_web_static import do_deploy
"""deploys the compressed archive to remote servers"""

def deploy():
    """calls dopack and do deployment"""
    archive_path = do_pack()
    result = do_deploy(archive_path)
    return result
