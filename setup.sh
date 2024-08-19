#!/bin/bash

python -m venv MyEnvironment
source /work/MyEnvironment/bin/activate
python -m pip install ipykernel
python -m ipykernel install --user --name=MyEnvironment
python -m pip install pingouin