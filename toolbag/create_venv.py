"""
Creates an up-to-date virtual environment.
"""
import subprocess
from typing import Optional


def create_venv(venv_dir: str = "venv", prompt_prefix: Optional[str] = None):
    """
    Create a new virtual environment.

    Create a new virtual environment using the standard library `venv` module in
    directory `venv_dir` with the possibility to give it an alternative prompt
    prefix `prompt_prefix`.

    Parameters
    ----------
    venv_dir : str
        The directory to create the environment in (default is "venv").
    prompt_prefix : str, optional
        An alternative prompt prefix for this environment (default is `venv_dir`).
    """
