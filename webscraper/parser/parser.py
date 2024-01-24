import urllib
from urllib import request
import traceback
import logging
import re

from bs4 import BeautifulSoup
from dto.event.Event import Event

PARSER_TYPE='html.parser'
TAG_CONTENT='ici'
TAG_DAY='ul'
TAG_EVENT='li'

listEvent = []

def retrieveEventList(url):
  html=""
  try:
    response = urllib.request.urlopen(url).read()
    html = BeautifulSoup(response,PARSER_TYPE)
    content = html.find(TAG_CONTENT)
    currentDayEvents = content.find(TAG_DAY)

    while currentDayEvents != None:
      event_date = currentDayEvents.previousSibling.strip()
      assert checkDate(event_date)

      eventsOfTheDate = generateListDayEvent(currentDayEvents,TAG_EVENT,event_date)
      break
      currentDayEvents = currentDayEvents.find_next_sibling('ul')
  except Exception as e:
    # logging.error(f"An exception occurred while trying to scrape the url: {url}")
    # logging.debug(e,exc_info=True)
    print(e)
  return html

#generate the list of Event objects
def generateListDayEvent(content,tagName,date):
  raw_eventsOfTheDay = content.find_all(tagName)
  TAG = '<'+tagName+'>'
  eventsOfTheDay = []
  while len(raw_eventsOfTheDay)>0:
    raw_event = raw_eventsOfTheDay.pop()
    event_str = str(raw_event)
    if(int(event_str.count(TAG)) == 1): #checks if event list is well formed
      event = BeautifulSoup(raw_event.decode_contents(), PARSER_TYPE)  #removes outer tag 'li'
      #eventsOfTheDay.append(event)
      generateEvent(date,event)
      continue
    else:
      indices = [index for index in range(len(event_str)) if event_str.startswith(TAG, index)]
      for i in range(len(indices)):
        if i==len(indices)-1:
          raw_event = event_str[indices[i]+len(TAG):]
        else:
          raw_event = event_str[indices[i]+len(TAG):indices[i+1]]
        event = BeautifulSoup(raw_event, PARSER_TYPE) #reformate event tag li and removes 'li' tag
        generateEvent(date,event)
        # eventsOfTheDay.append(event)
  return eventsOfTheDay

def generateEvent(date,bs4Tag):
  print(bs4Tag)
  event = Event()

  food_str = ""
  print(bs4Tag.get_text())
  if re.search('Restauration', bs4Tag.get_text(), re.IGNORECASE):
    print("ok") 
  event_link = bs4Tag.find('a')['href']
  event_type = re.sub(r'[()]', '', bs4Tag.i.string) #removes ()

  event.setLink(event_link) #check if multiple 'a'
  event.setType(event_type)
  event.setDate(date)
  print(event)
  return

def formatDate(date):
  return

def checkDate(text):
  regex=r"[A-zÀ-ú]+\s([0-9]){1,2}\s[A-zÀ-ú]+\s[0-9]{4}" #like Vendredi 12 Février 9090
  if (re.search(regex,text)):
    return True
  return False