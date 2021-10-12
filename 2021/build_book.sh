#!/bin/bash

# build html documents
jupyter-book build Book/


ghp-import -n -p -f Book/_build/html

