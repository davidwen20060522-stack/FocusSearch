import webbrowser

def Douyin(search):
    url_douyin = "https://www.douyin.com/search/"
    url_obj1 = url_douyin + search
    print("1")
    webbrowser.open_new(url_obj1)
