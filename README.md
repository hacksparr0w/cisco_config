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
