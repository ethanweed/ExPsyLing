# conda activate opensesame-py3

from osweb import data
from datamatrix import io

import os
import glob

pathin = 'PATH/TO/DATA'

os.chdir(pathin)

for file in glob.glob('*.txt'):
    filename = file[0:-4]
    dm = data.parse_jatos_results(
    jatos_path=pathin + file,
    include_context=True)
    io.writetxt(dm, filename + '.csv')