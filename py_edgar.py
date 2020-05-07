# https://github.com/joeyism/py-edgar
# pip install/uninstall edgar


from edgar.company import Company
from edgar.edgar import Edgar
from edgar.txtml import TXTML
from edgar.xbrl import XBRL, XBRLElement

company = Company("Oracle Corp", "0001341439")
tree = company.get_all_filings(filing_type="10-K")
docs = Company.get_documents(tree, no_of_documents=5)


company = Company("INTERNATIONAL BUSINESS MACHINES CORP", "0000051143")
doc = company.get_10K()
text = TXTML.parse_full_10K(doc)

edg = Edgar()
possible_companies = edg.find_company_name("Cisco System")

company = Company("Oracle Corp", "0001341439")
results = company.get_data_files_from_10K("EX-101.INS", isxml=True)
xbrl = XBRL(results[0])
result = XBRLElement(xbrl.relevant_children_parsed[15]).to_dict()  # returns a dictionary of name, value, and schemaRef
