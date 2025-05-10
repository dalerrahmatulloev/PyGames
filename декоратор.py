import webbrowser

def validate(func):
    def wrapper(url):
        if "http" in url:
            print("This is a URL")
            func(url)
        else:
            print("This is not a URL")
    return wrapper

@validate
def open_url(url):
    webbrowser.open(url)

open_url("http://example")