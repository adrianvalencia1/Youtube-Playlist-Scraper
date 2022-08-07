# Import the Python Libraries I need
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

import pandas_datareader as pdr
import datetime
from datetime import date

# Import BeautifulSoup and Requests library for web scrapping
from bs4 import BeautifulSoup
import requests

#
# This program is made to extract the names of a videos in a YouTube playlist
#

# Paste link to playlist below:
source = requests.get('https://www.youtube.com/playlist?list=PLkYCMRKILFANatMm2AS1M4X5Mr9Quz5Ld').text
soup = BeautifulSoup(source, 'lxml')

# Creating series for video names
nameSeries = pd.Series(dtype=float)

# Finding the amount of videos in the playlist
playlistSize = soup.find('div', {'class':'style-scope ytd-playlist-sidebar-primary-info-renderer'}).find('span', {'class': 'style-scope yt-formatted-string'})


#for 
#playlist = soup.find('div', {'class':'style-scope ytd-playlist-video-list-renderer'})
#videoName = soup.find('a', {'id':'video-title'}).a.string

# Print
print(playlistSize)
