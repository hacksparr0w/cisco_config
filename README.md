<h1 align="center">
  🛜🛠️ <code>cisco_config</code>
</h1>

> [!WARNING]  
> This project is currently in a very early stage of development and, as such,
> may change drastically at any given time.

`cisco_config` is a Python implementation of a robust parsing algorithm
capable of reliably loading and exporting the Cisco Configuration file format.
The module includes a low-level parsing toolkit alongside an extensive library
of predefiend, high-level utilities and presets tailored to specific Cisco
products, such as Cisco ASA.

## Features
 - [ ] :gear: Powerful low-level loading and dumping toolkit with friendly
 and informative error messages
 - [x] :tada: Standardized high-level command modeling API based on Pydantic
 models
 - [ ] :books: Extensive library of predefined command models
 - [ ] :joystick: CLI tools and utilities for manipulating Cisco configuration
 files on the fly

## Installation

You can install `cisco_config` using `pip`:

```bash
pip install git+https://github.com/hacksparr0w/cisco_config.git
```

## Usage

### CLI

```bash
Usage: cisco_config [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  load  Loads a Cisco configuration and prints the parsed commands as JSON
```

### Python API

 - `cisco_config.asa.load`

## Examples

### Defining a command model

```python
from typing import Literal, Optional

from cisco_config.command import Command, Key
from cisco_config.asa.common import dsl


class EnablePassword(Command):
    key: Key["enable", "password"]
    value: str
    level: Optional[dsl.level.Level] = None
    encryption: Optional[Literal["pbkdf2", "encrypted"]] = None

```

### Loading a configuration file

```python
import cisco_config.asa

version = "9.20"

with open("asa.conf", "r", encoding="utf-8") as source:
    commands = cisco_config.asa.load(version, source, strict=False)
```

### Other examples

For more examples, see the `tests` directory.

## Issues

Found bug or have an idea for a cool feature? Please, open an issue in our
issue tracker. Pull requests are also welcome!
