import webbrowser

def Douyin(search):
    url_douyin = "https://www.douyin.com/search/"
    url_obj1 = url_douyin + search
    webbrowser.open_new(url_obj1)

def Xiaohongshu(search):
    url_xiaohongshu = "https://www.xiaohongshu.com/search_result?keyword="
    url_obj2 = url_xiaohongshu + search
    webbrowser.open_new(url_obj2)

def Bilibili(search):
    url_bilibili = "https://search.bilibili.com/all?keyword="
    url_obj3 = url_bilibili + search
    webbrowser.open_new(url_obj3)

def Baidu(search):
    url_baidu = "https://wap.baidu.com/ssid=400c42616c6c6f7761676e6973g532601000000/s?word="
    url_obj4 = url_baidu + search
    webbrowser.open_new(url_obj4)
