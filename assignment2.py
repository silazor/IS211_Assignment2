import urllib.request

def downloadDATA(url):
    print(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print(html)
    return html

url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
print(downloadDATA(url))
