#!/usr/bin/env python
import sys
import feedparser
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description='Information about recently Dockerized people')
parser.add_argument('name', nargs='?', default=None,
                   help='Optional, name of the person you want to lookup')
parser.add_argument('-v', action='store_true',
                   help='optional, do you want the whole blog post')
args = parser.parse_args()

d = feedparser.parse('http://blog.docker.com/feed/')
for e in d.entries:
    for c in e.tags:
        if 'Dockerized' in c.term:
            if args.name and args.name not in e.author:
                continue
            print e.author
            print e.link
            print e.title
            if args.v:
                call(["/usr/local/bin/python",
                    "/usr/local/lib/python2.7/site-packages/reporter/reporter.py",
                    "--url",
                    e.link])
            continue
