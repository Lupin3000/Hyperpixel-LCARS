# Hyperpixel-LCARS

LCARS on Pimoronis [Hyperpixel](https://shop.pimoroni.com/search?q=hyperpixel) - Hi-Res display for Raspberry Pi written in Python3.

## Table of Contents

- [Note](#Note)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Usage](#Usage)

## Note

> Please note that the fonts are only available for private use! You can adapt, improve and use the source code for your projects as you wish. The author of this repository take no responsibility for your use or misuse or any damage on your devices!

## Requirements

```shell
# update system (optional)
$ sudo apt update && sudo apt upgrade -y

# install packages
$ sudo apt install -y build-essential vim git python3 python3-pip

# clone repository into home directory
$ git clone https://github.com/Lupin3000/Hyperpixel-LCARS.git ~/
```

## Installation

To make the installation a little easier for you, you can use the Makefile. If you want to do the installation by hand, take a look at the [Makefile](Makefile). All steps are explained there.

```shell
# change into repository
$ cd ~/Hyperpixel-LCARS/

# show Makefile (optional)
$ cat Makefile

# install LCARS for Hyperpixel 4.0 rectangle
$ make rectangle 

# install LCARS for Hyperpixel 2.1 round
$ make round

# install LCARS for Hyperpixel 4.0 square
$ make square
```

## Usage

### Configuration

> Modify api settings inside file `config.ini` before reboot!

```shell
# modify file
$ vim ~/Hyperpixel-LCARS/config.ini
```

You need a valid API KEY from [openweathermap.org](https://openweathermap.org/api).

```config.ini
[openweathermap.org]
apikey = abc123def456ghi789
zipcode = 8405
countrycode = CH
measurement = metric
```

### Autostart

If your application don't start automatically after reboot, verify correct fullpath to target.

```shell
# show specific settings
$ cat ~/.config/autostart/lcars.desktop | grep -i 'Exec*'
Exec=/usr/bin/python3 /home/pi/Hyperpixel-LCARS/src/FILE
```
