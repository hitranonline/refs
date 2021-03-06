from django.test import TestCase

# Create your tests here.

#pip install django==1.11.17

import os
import sys
#webapp_path = os.path.join('/Users/your_name/www/pyref')
webapp_path = os.path.join('/Users/your_name/pyref')
sys.path.append(webapp_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pyref.settings'
import django

django.setup()

from refs.models import Ref, get_ref_from_doi

doi = '10.1103/PhysRevA.85.032515'

ref = get_ref_from_doi(doi)

print(ref)

import requests
import json

token="Enter Your Token Here"
payload = {"bibcode": ["2019MNRAS.488.2332L"],
           "sort": "first_author asc",
           "format":
           '''{"ref_json": {"authors": "%I",
              "title": "%T",
              "journal": "%J",
              "volume": "%V",
              "start-page": "%p",
              "end-page": "%P",
              "year": %Y,
              "doi": "%d",
              "bibcode": "%u"}}'''
              }
r = requests.post("https://api.adsabs.harvard.edu/v1/export/custom", \
                 headers={"Authorization": "Bearer " + token, "Content-type": "application/json"}, \
                 data=json.dumps(payload))
response_json = r.json()
ref_json = json.loads(response_json['export'])['ref_json']

print('authors:', ref_json['authors'])
print('title:', ref_json['title'])
print('journal:', ref_json['journal'])
print('volume:', ref_json['volume'])
print('start-page:', ref_json['start-page'])
print('end-page:', ref_json['end-page'])
print('year:', ref_json['year'])
print('doi:', ref_json['doi'])
print('bibcode:', ref_json['bibcode'])

response_json['export']
