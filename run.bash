#!/bin/bash 
stdbuf -oL python3 faceExpress.py > output.txt
python read.py
