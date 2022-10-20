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
$ sudo apt install -y build-essential git python3 python3-pip

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

... t.b.d.
