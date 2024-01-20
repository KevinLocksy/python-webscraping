import urllib
from urllib import request
import traceback
import logging
import re

from bs4 import BeautifulSoup
from dto.event.Event import Event

listEvent = []

def retrieveEventList(url):
  html=""
  try:
    response = urllib.request.urlopen(url).read()
    html = BeautifulSoup(response,'html.parser')
    #print(html.prettify())
    content_tag='ici'
    content = html.find(content_tag)
    allelement = content.get_text(separator=';')
    current_ul = content.find('ul')
    last_ul = content.find_all("ul")[-1]

    while current_ul != None:
      date = current_ul.previousSibling
      assert checkDate(date)

      eventsOfTheDate = current_ul.find_all("li")
      for e in eventsOfTheDate:
        print("---- event -----")
        event = Event()
        #print(e.get_text(separator=';'))

        link_list = e.find_all('a')
        print(link_list)
        event.setDate(date)
        #event.setLink(link)
        listEvent.append(event)
      current_ul = current_ul.find_next_sibling('ul')
    getDate()
  except Exception as e: 
    logging.error(f"An exception occurred while trying to scrape the url: {url}")
    logging.debug(e,exc_info=True)
  return html

def getDate(dom):
  
  return ""

def formatDate(date):
  return

def getAddress(dom):
  return

def checkDate(text):
  regex=r"[A-zÀ-ú]+\s([0-9]){1,2}\s[A-zÀ-ú]+\s[0-9]{4}" #like Vendredi 12 Février 9090
  if (re.search(regex,text)):
    return True
  return False

def checkNewEvent(text):
  
  return 