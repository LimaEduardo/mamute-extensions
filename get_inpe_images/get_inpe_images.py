import requests

iconsNames = ['ec', 'ci', 'c', 'in', 'pp', 'cm', 'cn', 'pt', 'pm', 'np', 'pc', 'pn', 'cv', 'ch', 't', 'ps', 'e', 'n', 'cl', 'nv', 'g', 'ne', 'nd', 'pnt','psc', 'pcm', 'pct', 'pcn', 'npt', 'npn', 'ncn', 'nct', 'ncm', 'npm', 'npp', 'vn', 'ct','ppn','ppt', 'ppm']

print('Beginning file download with requests')

for name in iconsNames:
    url = 'http://s0.cptec.inpe.br/webdop/static/resources/common/assets/images/icones/tempo/icones-grandes/'+name+'.png'
    r = requests.get(url)

    with open('./'+name+'.png', 'wb') as f:  
        f.write(r.content)

    print(r.status_code)  
    print(r.headers['content-type'])  
    print(r.encoding)  
