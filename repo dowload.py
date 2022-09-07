import requests



url = f'https://github.com/codebasics/py/tree/master/DataScience/CelebrityFaceRecognition/model'
print('url:', url)

r = requests.get(url)

if r.status_code == 200:
    print('size:', len(r.content))
    with open(f'image classifer .zip', 'wb') as fh:
        fh.write(r.content)
    print(r.content[:10])  # display only some part
else:
    print(r.text)    