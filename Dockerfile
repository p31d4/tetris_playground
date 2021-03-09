FROM rust:1.78.0
# Distributor ID: Debian
# Description:    Debian GNU/Linux 12 (bookworm)
# Release:        12
# Codename:       bookworm

RUN export TERM=xterm-256color

RUN apt update

# versions got from apt-cache policy <package>
RUN apt install -y vim \
        git \
        lsb-release \
        screen \ 
        python3-pygame \
        pylint \
        libasound2-dev \
        libsdl2-dev \
        lynx

# Just in case I don't have internet connection
# Downloading to /usr/local/cargo/registry
RUN cd  /tmp && cargo new fetch_tetra && cd fetch_tetra && \
        cargo add tetra@0.8 && cargo fetch && cargo doc

RUN rustup component add clippy

# This would be a possibility, but takes too long
#RUN cargo vendor

#RUN cd /tmp && git clone https://github.com/libsdl-org/SDL.git -b SDL2 && cd SDL && \
#    mkdir build && cd build && ../configure && make && make install && make clean
