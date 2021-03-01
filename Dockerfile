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
        python3-pygame=2.1.2+dfsg-5+b1
