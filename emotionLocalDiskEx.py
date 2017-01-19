import time
import requests
import operator

### This script processes the emotion of an image saved on your local
### computer using microsoft's cognitive service's emotion API

_url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
_key = '*****generate key'
_maxNumRetries = 10


def processRequest(json, data, headers, params):
    retries = 0
    result = None

    while True:
        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )
        if response.status_code == 429: 
            print( "Message: %s" % ( response.json()['error']['message'] ) )
            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break
        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )
        break        
    return result

def get_strongest_emotion(raw_result):
    num_faces, res = len(raw_result), raw_result
    if num_faces < 1:
        return None
    elif num_faces == 1:
        return max(res[0]['scores'], key=(lambda s: res[0]['scores'][s]))
    else:
        return [max(face['scores'], key=(lambda s: face['scores'][s])) for face in res]


pathToFileInDisk = r'*****path to image'
with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/octet-stream'


result = processRequest(None, data, headers, None)

if result is not None:
    returnedEmotion = get_strongest_emotion(result)
    print returnedEmotion
    f = open('output.txt', 'w')
    f.write(returnedEmotion)
    f.close()
        


    
