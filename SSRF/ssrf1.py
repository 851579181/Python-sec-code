# -*- coding：utf-8 -*-
import requests

def yds(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        return "please input the right url"
