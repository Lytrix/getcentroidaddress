
import requests
import requests_cache
import csv
import sys

# ------------------------------------------------------------
# Get centroids of streetnames Amsterdam
# https://github.com/PDOK/locatieserver/wiki/API-Locatieserver
# ------------------------------------------------------------

# save api requests to temporary sqlite db for use with many reoccuring names
requests_cache.install_cache('requests_cache', backend='sqlite')  # , expire_after=180)

if len(sys.argv) == 1:
    print('You must give the csv filename as a command line argument after python getCentroidAddress.py ...')
    fileName = input('Enter Filename: ')
else:
    fileName = sys.argv[1]

# fileName = 'test'
csvName = fileName + '_coord.csv'
with open(fileName, 'r') as inputFile:
    header = False
    reader = csv.DictReader(inputFile, dialect='excel')
    with open(csvName, 'w') as outputFile:
        for row in reader:
            for fieldName in reader.fieldnames:
                if fieldName.lower() in ('straatnaam','adres','straat', 'openbareruimtenaam'):
                    try:
                        getUrl = "http://geodata.nationaalgeoregister.nl/locatieserver/free?q=%s AND woonplaatsnaam:Amsterdam&fl=centroide_ll,straatnaam,score" % row[fieldName]
                        result = requests.get(getUrl)
                        resultJson = result.json()
                        print(getUrl)
                        # print(resultJson['response'])
                        if result.status_code == 200 and resultJson['response']['numFound'] != 0:
                            for item in resultJson['response']['docs']:
                               if item['score'] == resultJson['response']['maxScore']:
                                    del item['score']
                                    row.update(item)
                        else:
                            print('No results found')
                    except result.status_code as E:
                        print(E)

                    w = csv.DictWriter(outputFile, row.keys())
                    if header == False:
                        w.writeheader()
                        header = True
                    w.writerow(row)
