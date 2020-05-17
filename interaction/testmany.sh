#!/bin/bash

for x in {1..1}; do
    source ~/.virtualenvs/ooo/bin/activate
    python3 ./check1.py lifebooox.lb.isroot.com 37452 > /tmp/adventure_testresults_${x}.log &

done

