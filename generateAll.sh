#!/bin/bash

cd Contents/Resources
rm -rf *.dsidx
python generateIndex.py
cd ../..
tar -cvzf concourse-ci.tgz --exclude=*.py Contents icon.png 
