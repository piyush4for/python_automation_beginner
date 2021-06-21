import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
res.raise_for_status()
playFile = open('romeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()