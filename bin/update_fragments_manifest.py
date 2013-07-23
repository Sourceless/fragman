#!/usr/bin/env python

'''
Update (rewrite) fragments manifest

Usage:
   python update-fragments-manifest <manifest_file> <fragments_path>
'''

import json
import sys
import os

def update_manifest(manifest_file, fragments_path):
    # Yes, there's too much here for a listcomp...
    fragments = [file_.rstrip('.py') for file_ in os.listdir(fragments_path)
                 if file_.endswith('.py') and not file_startswith('_')]
    manifest_file.write(json.dumps(fragments))
    # Can be redone later to include more metadata

if __name__ == '__main__':
    fragments_path = sys.argv[2]
    with open(sys.argv[1], 'w') as manifest:
        update_manifest(manifest, fragments_path)
