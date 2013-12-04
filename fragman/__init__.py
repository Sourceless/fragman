#!/usr/bin/env python
'''
Fragment Manager

'Downloads' and allows import of fragments
'''

import json
import importlib
import os.path

def pull(*fragments):
    for fragment in fragments:
        # In reality you'd get it from the package list...
        frag_path = "fragman.fragments." + fragment
        temp = __import__(frag_path, globals(), locals(), [fragment])
        shard = temp.__dict__[fragment]
        globals()[fragment] = shard
