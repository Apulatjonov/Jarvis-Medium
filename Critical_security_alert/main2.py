import requests

if __name__ == "__main__":
    URL = "http://api.brainshop.ai/get?bid=162049&key=sEN6FttC8GopL3fG&uid=[]&msg=hello"
    r = requests.get(URL)
    print(r.json()['cnt'])