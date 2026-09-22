from urllib.parse import quote,unquote
import searchway
import os

def welcome_page():
    print("========================================")
    print("             Focus Search")
    print("========================================")
    print(" ")
    print("           你现在想搜索什么？")
    print(" ")
    print("----------------------------------------")
    search = input(">")
    search_url = quote(search)
    os.system("cls")
    return search_url

def choose_page(search):


    print("========================================")
    print("              选择搜索平台")
    print("========================================")
    print(" ")
    print("          搜索：" + unquote(search))
    print(" ")
    print("          [1] 抖音")
    print("          [2] 小红书")
    print("          [3] b站")
    print("          [4] 百度")
    print("          [5] ALL")
    print(" ")
    print("----------------------------------------")
    n = input(">")
    if n == "1":
        searchway.Douyin(search)
    elif n == "2":
        searchway.Xiaohongshu(search)
    elif n == "3":
        searchway.Bilibili(search)
    elif n == "4":
        searchway.Baidu(search)
    elif n == "5":
        searchway.Douyin(search)
        searchway.Xiaohongshu(search)
        searchway.Bilibili(search)
        searchway.Baidu(search)
    else:
        print("选择有误！！仔细看！")
        value = "error"
        return value

    os.system("cls")
    print("========================================")
    print("              Finish!!!")
    print("========================================")
    input()

value = "1"
while True:
    search = welcome_page()
    value = choose_page(search)
    if (value == "error"):
        break
