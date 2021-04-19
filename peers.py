from time import sleep

import requests


DELAY = 60  # 1 minute

urls = {
    "index.html": "https://publicpeers.neilalexander.dev/",
    "publicnodes.json": "https://publicpeers.neilalexander.dev/publicnodes.json"
}


def get_content(url):
    content = None
    try:
        response = requests.get(url)
    except Exception as e:
        print("Shit happens!")
        print("{}: {}".fromat(e.__class__.__name__, e))
    else:
        if response.ok:
            content = response.content
    return content


def main():
    while True:
        for fname, url in urls.items():
            content = get_content(url)
            if not content:
                print("Shit happens, unexpected server response")
            with open(fname, "w"):
                f.write(content)
        sleep(DELAY)


if __name__ == "__main__":
    main()
