FROM base/archlinux  
MAINTAINER Manu Sánchez <manuel.sanchez@biicode.com>

# update base and install base-devel and multilib-devel
# and purge package cache for image size
RUN pacman -Syy --noconfirm
RUN pacman -S --needed --noconfirm base-devel git wget libunistring
RUN pacman-db-upgrade

RUN echo "nobody ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    
# Install yaourt:

RUN wget https://aur.archlinux.org/packages/pa/package-query/package-query.tar.gz
RUN ls -al
RUN tar zxvf package-query.tar.gz

WORKDIR package-query
RUN chown -R nobody .
RUN sudo -u nobody makepkg -si --noconfirm
WORKDIR ..

RUN curl -O https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz
RUN ls -al
RUN tar zxvf yaourt.tar.gz

WORKDIR yaourt
RUN chown -R nobody .
RUN sudo -u nobody makepkg -si --noconfirm
WORKDIR ..

# Install python:

RUN pacman -S python2 --noconfirm --needed

# Install aurploader:

RUN yaourt -S python3-aur --noconfirm

# Generate package

RUN git clone https://github.com/Manu343726/biicode-packages
WORKDIR biicode-packages/archlinux
RUN ./generate.sh
