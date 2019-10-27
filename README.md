# passgen

A command line secure password generator with customizable options.

## Installation

Run the installation script to create a symlink.
```
bash install.sh
```

Ensure that `$HOME/.local/bin` is in your PATH variable by adding the following to `~/.bashrc`.
```
export PATH=$HOME/.local/bin:$PATH
```

## Usage
```
passgen [-h] [--upper UPPER] [--lower LOWER] [--num NUM]
        [--special SPECIAL] [--toggle] [--duplicates]
        [difficulty]
```
Defaults to `passgen medium`.
