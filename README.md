ytsearch
========

A simple python utility that searches Youtube using the Youtube Data API. 
Created originally for usage with [my IRC bot, ubot.][1] but can be used separately.

Setup
--------

To use this program you must first create an API key as shown by [this video.][2]
You do not need to create an OAuth 2.0 client ID & secret, just an API key.

Once you've created the API key set it locally with either:

*NIX `export DEVELOPER_KEY="yourapikeygoeshere"`

Windows: `set DEVELOPER_KEY="yourapikeygoeshere"`

Lastly this program requires the `Google API Client Library for Python`
Available from `pip` or `easy_install`. Complete installation [instructions are available here.][3]
 
Usage
---------

Basic usage is as follows:

	>>> from ytsearch import youtubeSearch
	>>> query = 'Up Trailer'
	>>> youtubeSearch(query)
	'Title: UP Official Movie Trailer #3 | Link: http://youtu.be/pkqzFUhGPJg'


[1]: https://github.com/sleepyotaku/ubot/
[2]: https://www.youtube.com/watch?v=Im69kzhpR3I
[3]: https://developers.google.com/api-client-library/python/start/installation
