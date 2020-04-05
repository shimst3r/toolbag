"""
Creates an up-to-date virtual environment.
"""
import subprocess
import sys

import typer


def create_venv(
    venv_name: str = typer.Option(
        "venv", "--venv", help="Name of the new venv folder.", show_default=True
    ),
    prompt_prefix: str = typer.Option(
        None, "--prompt", help="Prompt prefix shown when the venv is activated."
    ),
):
    """
    Create a new virtual environment in the $PWD.

    Create a new virtual environment in the current directiry using the standard
    library `venv` module in directory `venv_name` with the possibility to give
    it an alternative prompt prefix `prompt_prefix`.

    After creating the virtual environment, its pip dependency is updated.
    """
    if not prompt_prefix:
        prompt_prefix = venv_name

    subprocess.run([sys.executable, "-m", "venv", venv_name, "--prompt", prompt_prefix])

    venv_executable = f"{venv_name}/bin/python"
    subprocess.run([venv_executable, "-m", "pip", "install", "--upgrade", "pip"])


if __name__ == "__main__":
    create_venv()
