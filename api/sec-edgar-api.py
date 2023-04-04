# pip install sec-edgar-api
from sec_edgar_api import EdgarClient

# Specify user-agent string to pass to SEC to identify
# requests for rate-limiting purposes
edgar = EdgarClient(user_agent="<Sample Company Name> <Admin Contact>@<Sample Company Domain>")

# Get submissions for Apple with the additional paginated files
# appended to the recent filings to prevent the need for extra
# manual pagination handling
s = edgar.get_submissions(cik="320193")


# Get submissions for Apple without automatic pagination handling,
# which requires manual handling of the paginated files (not recommended)
s1 = edgar.get_submissions(cik="320193", handle_pagination=False)


# Get company concept for Apple
c = edgar.get_company_concept(cik="320193", taxonomy="us-gaap", tag="AccountsPayableCurrent")


# Get company facts for Apple
f = edgar.get_company_facts(cik="320193")


# Get one fact for each reporting entity in specified
# calendar period (Q1 2019)
f = edgar.get_frames(taxonomy="us-gaap", tag="AccountsPayableCurrent", unit="USD", year="2019", quarter=1)
