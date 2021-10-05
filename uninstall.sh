#!/bin/bash

for i in $(ls $PWD/bin/)
do
    rm -f ~/.local/bin/$i
done
