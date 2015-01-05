FROM base/archlinux
MAINTAINER Manu Sánchez <manuel.sanchez@biicode.com>


# System upgrade:

RUN pacman -Syu --noconfirm --needed

# Install git:

RUN pacman -S git --noconfirm --needed

# Install base-devel:

RUN pacman -S base-devel --noconfirm --needed

# Install yaourt:

RUN mkdir yaourt-build

RUN curl -O https://aur.archlinux.org/packages/pa/package-query/package-query.tar.gz
RUN tar zxvf package-query.tar.gz
WORKDIR package-query
RUN makepkg -si --asroot
WORKDIR ..
RUN curl -O https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz
RUN tar zxvf yaourt.tar.gz
WORKDIR yaourt
RUN makepkg -si --asroot
WORKDIR ../..

# Install python:

pacman -S python2 --noconfirm --needed

# Install aurploader:

RUN yaourt -S python3-aur --noconfirm
