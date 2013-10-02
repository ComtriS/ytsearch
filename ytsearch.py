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


from apiclient.discovery import build


devKey = open("api-key", "r").read()
#devKey = 'AIzaSyDGS3Hr4o_SJDFn1kjRy-EylAiFJcUigRU'
api_name = "youtube"
youtube_api_version = "v3"


def youtubeSearch(query):
    youtube = build(api_name,
                    youtube_api_version,
                    developerKey=devKey)
    search_response = youtube.search().list(
        maxResults=1,
        part="id,snippet",
        q=query
    ).execute()


    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video = " Youtube Result: %s (%s) " % (search_result["snippet"]["title"],
                                                   "http://youtu.be/" +
                                                   search_result["id"]["videoId"])
        else:
            return "Video not found."

    #video = video.decode()

    return video.encode('ascii', 'ignore')
