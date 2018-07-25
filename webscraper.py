# Download 100 xkcd comics
import os, bs4, requests
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
count = 0
while not url.endswith('#'):
    # Download  page
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Download failed at %s, because of %s' % (url, exc))
    soup = bs4.BeautifulSoup(res.text)
    # Find url
    comicElem = soup.select('#comic img')
    if comicElem:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download img
            print('Downloading img %s ...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this one
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        # Save img to xkcd
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as ImageFile:
            for chunk in res.iter_content(100000):
                ImageFile.write(chunk)
    else:
        print('Could ot find image')
    # get prv button
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    # end at some point
    count = count+1
    if count == 1:
        url = '#'
print('Done')
