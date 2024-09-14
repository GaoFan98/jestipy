#!/bin/bash

for test_file in tests/*.py; do
    python3 cli.py "$test_file"
done
