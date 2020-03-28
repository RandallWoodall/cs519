# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randall Woodall
# March 27, 2020
# solar_scrub.py
# We have solar data as a collection of files that we need five values from.  This script will clean the files how we
# need them.

import pandas as pd

files = [pd.read_csv(x.strip(), header=None) for x in open('solar_files', 'r').readlines()]
outfiles = [open(x.strip(), 'w') for x in open('solar_files_out', 'r').readlines()]

for j in range(len(files)):
    p1 = files[j][25].rolling(12).mean()
    p2 = files[j][26].rolling(12).mean()
    p3 = files[j][27].rolling(12).mean()
    # just write straight to a file.
    m_count = 0;
    outfiles[j].write('time,power\n')
    for i in range(12, len(p1), 12):
        outfiles[j].write(str(i // (60 * 12)).zfill(2) + ':' + str(i // 12 % 60).zfill(2) + ':00, ')
        outfiles[j].write(str(p1[i] + p2[i] + p3[i]))
        outfiles[j].write(',\n')
    outfiles[j].close()

