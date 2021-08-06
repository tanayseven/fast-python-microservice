import subprocess

import click


@click.command()
@click.option("--host", default="0.0.0.0")
@click.option("--port", default=8080)
def dev(host, port):
    """Create a new user"""
    click.echo("Running server in dev mode")
    completed = subprocess.run(
        f"poetry run uvicorn src.main:app --host {host} --port {port} --reload",
        shell=True,
        executable="/usr/bin/zsh",
    )
    exit(completed.returncode)
