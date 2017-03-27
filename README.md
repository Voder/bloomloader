**bloomloader**

A simple python script to download timelapse videos from [Bloomsky](http://www.bloomsky.com) weather station.  
Downloads the last available timelapse video for the weather station identified through the api key.

*Install required lib:*  
`pip install requests`  

*To configure:*  
- enter your bloomsky api key in the script (*mandatory*)  
`api_key = "===== INSERT YOUR API KEY HERE ====="`
- units  
`intl = True / False`
- target filename  
*default:* `timelapse-<yyyy-MM-dd>.mp4`  

*To run:*  
`python loadTimelapse.py`
