#!/usr/bin/env python3
# 安裝pytube的方式：pip install git+https://github.com/nficano/pytube.git
import os
import pytube
import urllib.request
import re
import time
from googleapiclient.discovery import build

# 申請Youtube Data API key
# https://hackmd.io/@c36ICNyhQE6-iTXKxoIocg/S1eYdtA1P
api_key='AIzaSyAldObC55whNHf7Zx3gwj-e0BSDjYIi7Ps'

youtube = build('youtube', 'v3', developerKey=api_key)

MAX_COUNT = 1
nextPageToken =  None

# 設定搜尋關鍵字
search_by = 'naked yoga'

# 搜尋影片id
#while True:
videoList = []
for times in range(40): #會超過query上限
    req = youtube.search().list(q=search_by, part='snippet', videoDuration='any', type='video', maxResults=MAX_COUNT, pageToken=nextPageToken)
    res = req.execute()
    nextPageToken = res['nextPageToken']
    items = res['items']
    ##print(items)
    if res['nextPageToken'] == None:
        break; # exit from the loop
    for each_item in items:
        #store in DB or file or print the same.
        #print(each_item['id']['videoId'])
        videoList.append(each_item['id']['videoId'])

#print("\n",videoList,"\n")

# 以關鍵字建立影片儲存資料夾
download_location = "./Video"
videoSubFOlder = download_location + '/' + search_by.replace(' ', '-')

if not os.path.exists(videoSubFOlder):
    os.makedirs(videoSubFOlder)

# 逐一下載
print("==================================")
print(len(videoList)," videos found.")
print("==================================")
item = 1
for vid in videoList:
    itemurl = 'https://www.youtube.com/watch?v=' + vid
    print('Downloading video', item, '/', len(videoList) , '...', vid)
    try:
        yt = pytube.YouTube(itemurl)
        yt.streams.first().download(output_path=videoSubFOlder, filename=vid)
        item = item + 1
    except:
        print("Error... QQ... ")
print("==================================")
print("Done. ", item, "/", len(videoList)," videos downloaded.")
print("==================================")

