#!/bin/bash

cd concourse-ci.docset/Contents/Resources
rm -rf *.dsidx
python generateIndex.py
cd ../../..
rm -rf *.tgz
tar -cvzf concourse-ci.tgz --exclude=*.py concourse-ci.docset
