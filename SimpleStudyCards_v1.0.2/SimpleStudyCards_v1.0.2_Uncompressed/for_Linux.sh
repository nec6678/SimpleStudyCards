#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

python3 pythonscript/SimpleStudyCards_app.py

read