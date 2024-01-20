import sys
import argparse
import logging
from parser import *

#https://blog.sentry.io/logging-in-python-a-developers-guide/
logging.basicConfig(level=logging.ERROR,filename='logging.log',filemode='a',format="%(asctime)s %(levelname)s %(message)s")

if len(sys.argv) == 1:
  url = sys.argv[1]
else:
  url = "https://trad75.fr/"
   
def main(*args):
  res = retrieveEventList(url)

if __name__ == "__main__":
  argParser = argparse.ArgumentParser(description="Web scraping")
  argParser.add_argument("-u","--url", required=False, type=str, help='Url of the website to scrape. Default value:')
  args = argParser.parse_args()

  if args.url:
    url = args.url
    main(url)

