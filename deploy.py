#!/usr/bin/python3

import urllib.request, json 
import os

print(os.environ)

artifact_tag = os.environ['INCOMING_HOOK_BODY']
token = os.environ['GITHUB_TOKEN']

urlbase = 'https://api.github.com/repos/jricher/gnap-core-protocol/actions/artifacts'

with urllib.request.urlopen(urlbase) as url:
    data = json.loads(url.read().decode())

    for a in data['artifacts']:
        if a['name'] == os.environ.artifact_tag:
            print('Downloading artifact %s' % artifact_tag)
            
            req = urllib.request.Request(a['archive_download_url'], headers={
                'Authorization: Bearer ' + token
            })
            
            with urllib.request.urlretrieve(req) as local_filename, headers:
                print('Saved as: %s' % local_filename)
