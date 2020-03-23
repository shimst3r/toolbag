# toolbag

[![Latest PyPI version](https://img.shields.io/pypi/v/toolbag.svg)](https://pypi.python.org/pypi/toolbag/) [![PyPI license](https://img.shields.io/pypi/l/toolbag.svg)](https://pypi.python.org/pypi/toolbag/) [![PyPI format](https://img.shields.io/pypi/format/toolbag.svg)](https://pypi.python.org/pypi/toolbag/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/toolbag.svg)](https://pypi.python.org/pypi/toolbag/) [![PyPI status](https://img.shields.io/pypi/status/toolbag.svg)](https://pypi.python.org/pypi/toolbag/)

Python toolbag, like a toolbox, but more flexible!

## Usage

`toolbag` is a jack-of-all-trades package for Python automation. This includes automating your Python workflows (e.g. creating and populating virtual environments) and workflows managed by Python (e.g. cloud deployments our CI/CD pipelines).

It is a CLI based on the [typer](https://github.com/tiangolo/typer) framework.

## Installation

You can install the latest version via `pip`:

```shell
python -m pip install toolbag
```

Or you can clone the repository and build it from source:

```shell
git clone git@github.com:shimst3r/toolbag.git
cd toolbag
python -m venv venv --prompt toolbox
source venv/bin/activate
python setup.py install
```

## Quality Assurance

In order to keep the code quality high, the following actions will be implemented (using GitHub Actions):

* Checking the code with `black --check`,
* Checking the types with `mypy` (use type annotations!),
* Linting the code with `flake8` (because it's more forgiving than `pylint`),
* Testing the code with `pytest`.

## Compatibility

`toolbag` supports Python 3.7 and upwards.

## Licence

```
The MIT License (MIT)

Copyright (c) 2020 Nils Müller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Authors

`toolbag` was written by [Nils Müller](mailto:shimst3r@gmail.com).
