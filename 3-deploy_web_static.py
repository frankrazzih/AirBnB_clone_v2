#!/usr/bin/python3
# full deployment


def deploy():
    """Create and distribute an archive to a web server."""
    archive_path = do_pack()
    result = do_deploy(archive_path)
    return result
