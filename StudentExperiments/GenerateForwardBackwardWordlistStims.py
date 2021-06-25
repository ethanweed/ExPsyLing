import random

import os
pathin = '/Users/ethan/Desktop/'
file = 'Wordlist.txt'


os.chdir(pathin)

with open(file,'r') as f:
    text = f.read()

text = text.split('\n')

# wordlists with 4 words
num = 4
for j in range(15):
    n = []
    for i in range(num):
       ns = random.choice(text)
       n.append(ns)
    f = " ".join(n)
    r = list(reversed(n))
    r = " ".join(r)
    print(str(num)+', ', (f), ", forward, ", (f))
    print(str(num)+', ', (f), ", backward, ", (r))

# wordlists with 5 words
num = 5
for j in range(15):
    n = []
    for i in range(num):
       ns = random.choice(text)
       n.append(ns)
    f = " ".join(n)
    r = list(reversed(n))
    r = " ".join(r)
    print(str(num)+', ', (f), ", forward, ", (f))
    print(str(num)+', ', (f), ", backward, ", (r))

# wordlists with 6 words
num = 6
for j in range(15):
    n = []
    for i in range(num):
       ns = random.choice(text)
       n.append(ns)
    f = " ".join(n)
    r = list(reversed(n))
    r = " ".join(r)
    print(str(num)+', ', (f), ", forward, ", (f))
    print(str(num)+', ', (f), ", backward, ", (r))