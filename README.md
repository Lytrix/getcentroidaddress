# get Centroid Lat Lon from Address Name in Amsterdam #

Python script to add Centroid coordinates of streets to a CSV file containing address names using: 
https://github.com/PDOK/locatieserver/wiki/API-Locatieserver

### Install procedure ###

```
git clone https://github.com/lytrix/getcentroidaddress.git
virtualenv --python=$(which python3) venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python getCentroidAddress.py example/test.csv

```
This wil return a test_coord.csv file with added coordinates
