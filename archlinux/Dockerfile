FROM base/archlinux  
MAINTAINER Manu Sánchez <manuel.sanchez@biicode.com>

# update base and install base-devel and multilib-devel
# and purge package cache for image size
RUN pacman -Syy --noconfirm
RUN pacman -S --needed --noconfirm base-devel git wget libunistring
RUN pacman-db-upgrade

RUN echo "nobody ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Install python:
RUN pacman -S --noconfirm python2    

# Install aurploader:

RUN wget http://xyne.archlinux.ca/projects/python3-aur/src/python3-aur-2014.12.tar.xz
RUN ls -al
RUN tar zxvf python3-aur.tar.xz

WORKDIR python3-aur
RUN chown -R nobody .
RUN sudo -u nobody makepkg -si --noconfirm
WORKDIR ..
