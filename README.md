# g0dray.py
Author: Michele 'an4cr0n' Biondi

Version: 0.4

Description: Emulates xbacklight in software using xrandr.

Use cases:
  - Xbacklight doesn't work and responds like this (e.g. On Debian 'Stretch' and i3wm) 
    ```
    $ xbacklight
    No outputs have backlight property
    ```


## Usage
```
g0dray.py -h # Full list of options
```

## Install
Clone this repo and inside cloned directory run the installer like this:
```
sudo sh install.sh
```

## Work in progress (future releases)
- [x] Initial basic functions: get,set,inc,dec
- [x] Adding check for actions
- [ ] Installer
  - [x] source
  - [ ] .deb package
  - [ ] .rpm package
- [ ] Uninstaller
- [ ] Advanced functions
  - [x] time
  - [ ] steps
