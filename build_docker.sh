#!/bin/zsh

# docker build --tag <name:tag> - < Dockerfile
docker build --file Dockerfile --tag tetris_playground:0.1 .
