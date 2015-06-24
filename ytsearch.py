# Please note that this requires "Google APIs Clinet Library for Python".
#
# Available from easy_install:
#       $ easy_install --upgrade google-api-python-client
#
# Or available using pip:
#       $ pip install --upgrade google-api-python-client
#
# Depending on your system you may require root privileges
# to install the required library.

import os
from apiclient.discovery import build


DEV_KEY = os.environ.get("DEVELOPER_KEY")
API_NAME = "youtube"
API_VERSION= "v3"


def youtubeSearch(query):
    youtube = build(API_NAME,
                    API_VERSION,
                    developerKey=DEV_KEY)
    search_response = youtube.search().list(
        maxResults=1,
        part="id,snippet",
        q=query
    ).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video = "Title: %s | Link: %s" % (search_result["snippet"]["title"],
                                                   "http://youtu.be/" +
                                                   search_result["id"]["videoId"])
        else:
            return "Video not found."

    return video.encode('ascii', 'ignore')
