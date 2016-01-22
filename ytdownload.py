#!/usr/bin/python

from __future__ import unicode_literals

import os
import sys
import youtube_dl
from apiclient.discovery import build

DEV_KEY = os.environ.get("DEVELOPER_KEY")
API_NAME = "youtube"
API_VERSION= "v3"

def youtubeSearch(query, definition):
	youtube = build(API_NAME, API_VERSION, developerKey=DEV_KEY)
	search_response = youtube.search().list(maxResults=1, part="id,snippet", q=query, videoDefinition=definition, type="video").execute()

	for search_result in search_response.get("items", []):
		if search_result["id"]["kind"] == "youtube#video":
			link = "http://youtu.be/" + search_result["id"]["videoId"]

	if link:
		return link.encode('ascii', 'ignore')

if len(sys.argv) < 3 or len(sys.argv) > 4 :
	print "Usage: ytdownload.py SEARCH_TERM OUTPUT_DIR [RES]"
	sys.exit(1)

query = sys.argv[1]
out = sys.argv[2]
res = "high"
if len(sys.argv) > 3:
	res = sys.argv[3]

if not os.path.isdir(out):
	print "ERROR:", out, "does not exist!"
	sys.exit(1)

try:
	os.chdir(out)
except:
	print "ERROR: Couldn't change dir to", out
	sys.exit(1)

if "http://" in query:
	url = query
else:
	url = youtubeSearch(query, res)

if url is None and res == "high":
	res = "any"
	url = youtubeSearch(query, res)

if url is None:
	print "Failed to find", query
	sys.exit(1)

if res == "high":
	print "Found a HD version at", url
else:
	print "Found a SD version at", url

ydl_opts = {
	'writesubtitles': True,
	# 'noplaylist': True,
	# 'listformats': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])