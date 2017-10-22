# g0dray.py
Author: Michele 'an4cr0n' Biondi

Version: 0.8

Description: Emulates xbacklight in software using xrandr.

Use cases:
  - Xbacklight doesn't work and responds like this (e.g. On Debian 'Stretch' and i3wm) 
    ```
    $ xbacklight
    No outputs have backlight property
    ```


## Usage
```
usage: g0dray.py [-h] [-set percent | -inc percent | -dec percent | -get]
                 [-steps number] [-time milliseconds] [-help] [--version]

optional arguments:
  -h, --help          show this help message and exit
  -set percent        Sets brightness to the specified level.
  -inc percent        Increases brightness by the specified amount.
  -dec percent        Decreases brightness by the specified amount.
  -get                Print out the current backlight brightness of each
                      output with such a control. The brightness is
                      represented as a percentage of the maximum brightness
                      supported.
  -steps number       Number of steps to take while fading. Default is 20
  -time milliseconds  Length of time to spend fading the backlight between old
                      and new value. Default is 200.
  -help               Print out a summary of the usage and exit.
```

## Install
Clone this repo and inside cloned directory run the installer like this:
```
sudo sh install.sh
```

On Debian/Ubuntu install using the .deb file like this:
```
sudo dpkg -i g0dray_<major_version>.<minor_version>-<package_revision>.deb
```

## Uninstall
Go to /opt/g0dray.py/ and inside the folder type:
```
sudo sh uninstall.sh
```

## Work in progress (future releases)
- [x] Initial basic functions: get,set,inc,dec
- [x] Adding check for actions
- [ ] Installer
  - [x] source
  - [x] .deb package
  - [ ] .rpm package
- [x] Uninstaller
- [x] Advanced functions
  - [x] time
  - [x] steps
