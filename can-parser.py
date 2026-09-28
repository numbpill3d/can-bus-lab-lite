#!/usr/bin/env python3
# can-parser.py
import sys, collections
ids = collections.Counter()
with open(sys.argv[1]) as f:
    for line in f:
        if '#' in line:
            try:
                cid = line.split('#')[0].split()[-1]
                ids[cid] += 1
            except Exception:
                pass
for cid, n in ids.most_common(30):
    print(f"{cid:>10}  {n}")
