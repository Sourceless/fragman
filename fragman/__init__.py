#!/usr/bin/env python
'''
Fragment Manager

'Downloads' and allows import of fragments
'''

import json
import importlib
import os.path

def import_fragments(*fragments):
    for fragment in fragments:
        # In reality you'd get it from the package list...
        frag_path = "fragman.fragments." + fragment
        frag_func = __import__(frag_path).gloabls()[fragment]
        globals()[fragment] = frag_func
