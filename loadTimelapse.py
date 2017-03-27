import requests
import urllib
import datetime

# Bloomsky API URL
base_url = "https://api.bloomsky.com/api/skydata/"
# international units?
intl = True
# API key
api_key = "===== INSERT YOUR API KEY HERE ====="

# init target filename with date
today = datetime.date.today()
target = "timelapse-" + str(today) + ".mp4"


# read bloomsky data from base_url and return the json data
def getBloomskyData():
    url = base_url + ("?unit=intl" if intl else "")
    req = requests.get(url, headers={'Authorization': api_key})
    if req.status_code == 200 or req.status_code == 304:
        return req.json()
    else:
        print 'Error status code: ', req.status_code


# read the bloomsky json and return last element in VideoList array
def getLastTimelapseUrl(bloomsky_data):
    video_arr = bloomsky_data[0][u'VideoList']
    return video_arr[-1]



# get bloomsky data
bloomsky_data = getBloomskyData()
# get url of last timelapse video
video_url = getLastTimelapseUrl(bloomsky_data)
print "Found current video: ", video_url
print "Start downloading ..."
# download timelapse video
urllib.urlretrieve(video_url, target)
print "Target file: ", target
print "Download finished!"