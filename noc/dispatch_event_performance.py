#!/usr/bin/env python

import json
from pprint import pprint

with open('dispatch_events.json') as f:
    data = json.load(f)

    import pdb
    pdb.set_trace()


pprint(data)

