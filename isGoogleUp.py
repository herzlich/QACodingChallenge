# isGoogleUp
# Initial version: 10/2/2020 - Larry Herzlich
# Purpose - QA Coding challenge part 1
# Inputs: None
# Outputs: standard output text
# Local vars
mySite = "http://www.google.com"
invalidSite = "http://foo.bar.com"
# Side effects / Issues:
#      Website should be an input parameter
#      No retries enabled
#      Should be a callable function for reuse
#      
# Import Libraries
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# =================================================
# from stackoverflow example - actually contacts website 
# versus just contacting DNS server
# =================================================
req = Request(mySite)
# req = Request(invalidSite)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print ('Website ' + mySite + ' is UP!')