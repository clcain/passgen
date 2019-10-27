# passgen

## Installation

Run the installation script to create symlink.
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
