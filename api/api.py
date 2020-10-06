# import our libraries
import requests
import urllib
from bs4 import BeautifulSoup



# define a base url, this would be the EDGAR data Archives
from api.edgar_urls import *


cik_num = '886982'

company_url = BASE_URL + "/" + cik_num


# Get a single filing number, this way we can request all the documents that were submitted.
filing_number = "000156459020045871"
url = FILING_BY_COMPANY_URL_TMPL.format(cik_num, filing_number)



