import requests
import json
import sys


metadata_url = "http://169.254.169.254/latest/meta-data"
print "This program  queries the instance metadata and outputs the response in a json format"
print "Usage: get-instance-metadata.py [type]"
print "For example, to retrieve the instance hostname, execute get-instance-metadata.py hostname-name"
print "For full details, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html"

if len(sys.argv) > 1:
    # This should sanitise the input before appending it to the url
    # for security purposes, and to ensure that the parameter is valid
    metadata_url = metadata_url + "/" + sys.argv[1]

response = requests.get(metadata_url)

print json.dumps(response.text)

