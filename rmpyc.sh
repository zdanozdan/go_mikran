#!/bin/sh
echo "recursively removing compiler python files"
pwd
find ./ -name '*.pyc' -exec rm '{}' \; -print -or -name ".*.pyc" -exec rm {} \; -print
