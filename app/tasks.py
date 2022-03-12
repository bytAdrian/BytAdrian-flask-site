from urllib import request
from bs4 import BeautifulSoup
import time
import lxml


def scrape_synomyns(keyword):

  start = time.time()

  r = request.urlopen(f'https://www.thesaurus.com/browse/{keyword}')

  soup = BeautifulSoup(r.read().decode(), "lxml")

  kwords = [p.text for p in soup.select('a[href^="/browse/"]', href=True, limit=16)]

  end = time.time()
  time_elapsed = end - start
  
  print(kwords)
  print(f"time elapsed {time_elapsed}")

  return kwords