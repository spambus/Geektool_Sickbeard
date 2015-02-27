#!/usr/bin/env python
# encoding: utf-8
import json
from urllib2 import Request, urlopen, URLError
import datetime

# your sickbeard settings go here:
sburl = '127.0.0.1'
sbport = '8081'
apikey = 'yourapikeyhere'

now = datetime.datetime.now()
day = now.strftime("%A")

request = Request('http://' + sburl + ':' + sbport + '/api/' + apikey + '/?cmd=future&sort=date&type=today|missed')

# shows you want to hide from displaying
keywords = ['Seriename']

tmp = []

try:
    response = urlopen(request)
    tv_shows = json.loads(response.read())
    for show_data in tv_shows['data']['missed']:
        if tmp.__contains__(show_data['show_name']): 
           continue
        else:
           tmp.append(show_data['show_name'])
           if not any(word in show_data['show_name'] for word in keywords):
               print show_data['show_name']

    if dag == "Sunday":
       print "Maandag:"
    if dag == "Monday":
       print "Dinsdag:"
    if dag == "Tuesday":
       print "Woensdag:"
    if dag == "Wednesday":
       print "Donderdag:"
    if dag == "Thursday":
      print "Vrijdag:"
    if dag == "Friday":	
      print "Zaterdag:"
    if dag == "Saturday":
      print "Zondag:"

    for show_data in tv_shows['data']['today']:
        if tmp.__contains__(show_data['show_name']): 
           continue
        else:
           tmp.append(show_data['show_name'])  
           if not any(word in show_data['show_name'] for word in keywords):
              print show_data['show_name']

except URLError, e:
    print ('Error')
