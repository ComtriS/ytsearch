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
        else:
            return

    return link.encode('ascii', 'ignore')

if len(sys.argv) != 2:
	print "Usage: ytdownload.py SEARCH_TERM"
	sys.exit(1)

query = sys.argv[1]

url = youtubeSearch(query, "high")
if url is None:
	url = youtubeSearch(query, "any")

ydl_opts = {
	'writesubtitles': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])