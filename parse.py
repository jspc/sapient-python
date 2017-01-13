#!/usr/bin/env python

import argparse
import sys

from git_parse import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Grok and parse some noddy html')
    parser.add_argument('f', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    data = parser.parse_args().f

    print( app.App(data.read()).grok() )
