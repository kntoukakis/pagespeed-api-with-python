import requests
import json
import csv
from time import sleep

API_Key = "your-api-key"
baseURL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="

def get_pagespeed(API_Key, page_URL, baseURL, strategy):

    response_url = baseURL+page_URL+'&key='+API_Key+'&strategy='+strategy
    response = requests.get(response_url)
    json_data = response.json()

    lighthouseResult = json_data["lighthouseResult"]
    categories = lighthouseResult["categories"]
    performance = categories["performance"]
    score = performance["score"]
    return (score*100)
    sleep(1)


myFile = open('url_list.csv','r')
outputFile = open('results/pagespeed_results.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
reader = csv.reader(myFile)

outputWriter.writerow(["URL","Desktop Pagespeed","Mobile Pagespeed"])

for row in reader:
    url = row[1]
    if url == "URL":
        pass
    else:
        try:

            # measure for www over https
            # /// code ///

            desktop_pagespeed = get_pagespeed(API_Key, url, baseURL, "desktop")
            mobile_pagespeed = get_pagespeed(API_Key, url, baseURL, "mobile")
            print (url, desktop_pagespeed, mobile_pagespeed)

            outputWriter.writerow([url,desktop_pagespeed,mobile_pagespeed])
        except:
            outputWriter.writerow([url, "Error", "Error"])
            print('ERROR WITH URL: ', url)

myFile.close()
outputFile.close()