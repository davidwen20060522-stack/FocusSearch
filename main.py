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
    print(" ")
    print("----------------------------------------")
    n = input(">")
    if n == "1":
        searchway.Douyin(search)
    os.system("cls")
    print("========================================")
    print("              Finish!!!")
    print("========================================")
    input()

search = welcome_page()
choose_page(search)
