# thanks to michedini and their post at:
# https://forum.cogsci.nl/discussion/8257/problem-with-jatos-result-conversion

import jsonlines
import pandas as pd

raw = 'path/to/JATOS/json'
pathout = 'path/to/csv/output_file.csv'

i = 0

with jsonlines.open(raw) as reader:
    for line in reader:
        if i == 0:
            df = pd.DataFrame(line)
            i += 1
        else:
            df = pd.concat([df, pd.DataFrame(line)])
            i += 1

df['url'] = df['url'].ffill()
df['url'] = [int(x['srid']) for x in list(df['url'])]
del df['meta']
df.to_csv('pathout')