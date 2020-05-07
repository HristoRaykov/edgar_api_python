# https://github.com/coyo8/sec-edgar
from secedgar.filings import CIKLookup, Filing, FilingType

lookup = '0000320193'
lookups = CIKLookup(['aapl', 'msft', 'Facebook'])

my_filings = Filing(cik_lookup=lookup, filing_type=FilingType.FILING_10Q)

my_filings.save('tempdir')