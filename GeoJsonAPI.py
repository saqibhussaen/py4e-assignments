import urllib.request, urllib.parse, urllib.error
import json

service = 'http://py4e-data.dr-chuck.net/json?'
api_key = False

if api_key is False:
    api_key = 42

    
while True:
    inp = input('Enter Location-- ')
    if len(inp) < 1:
        print('Invalid Location')
        break
#dict to be merge with api key        
    para = dict()
    para['address'] = inp
    
    if api_key is not False:
        para['key'] = api_key
        
    merge = service + urllib.parse.urlencode(para)
    print('Extracting Data from', merge)
    
    url = urllib.request.urlopen(merge)
    hdle = url.read().decode()
    print('Extracted', len(hdle), 'characters')
#    print(hdle)
    try:
        data = json.loads(hdle)
    except:
        data = None
    
    if data['status'] !='OK':
        tem = input('Something went wrong!!, Do you still want to see data (Y/N)')
        if tem == 'Y':
            print(hdle)
            continue
        else:
            continue
#    print(json.dumps(data, indent=4))
    print(data['results'][0]['place_id'])