#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: python dos2unix.py
"""

import sys
"""
original = 'word_data.pkl'
destination = "word_data_unix.pkl"

original = 'python2_lesson06_keys.pkl'
destination = 'python2_lesson06_keys_unix.pkl'

original = "python2_lesson13_keys.pkl"
destination ="python2_lesson13_keys_unix.pkl"
"""
original = "python2_lesson14_keys.pkl"
destination ="python2_lesson14_keys_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))
