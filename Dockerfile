FROM rust:1.78.0
# Distributor ID: Debian
# Description:    Debian GNU/Linux 12 (bookworm)
# Release:        12
# Codename:       bookworm

RUN export TERM=xterm-256color

RUN apt update

# versions got from apt-cache policy <package>
RUN apt install -y vim=2:9.0.1378-2 \
        git=1:2.39.2-1.1 \
        lsb-release=12.0-1 \
        screen=4.9.0-4 \ 
        python3-pygame=2.1.2+dfsg-5+b1 \
        pylint=2.16.2-2 \
        libasound2-dev=1.2.8-1+b1 \
        libsdl2-dev=2.26.5+dfsg-1 \
        lynx=2.9.0dev.12-1

# Just in case I don't have internet connection
# Downloading to /usr/local/cargo/registry
RUN cd  /tmp && cargo new fetch_tetra && cd fetch_tetra && \
        cargo add tetra@0.8 && cargo fetch && cargo doc

RUN rustup component add clippy

# This would be a possibility, but takes too long
#RUN cargo vendor

#RUN cd /tmp && git clone https://github.com/libsdl-org/SDL.git -b SDL2 && cd SDL && \
#    mkdir build && cd build && ../configure && make && make install && make clean
