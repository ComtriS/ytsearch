#!/usr/bin/python

from __future__ import unicode_literals

import os
import sys
from ytsearch import youtubeSearch
import youtube_dl

if len(sys.argv) != 2:
	print "Usage: ytdownload.py SEARCH_TERM"
	sys.exit(1)

query = sys.argv[1]
result = youtubeSearch(query)
idx = result.find("Link: ") + len("Link: ")
url = result[idx:]

ydl_opts = {
	'writesubtitles': True,
	'noplaylist': True,
	#'listformats': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])