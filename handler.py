import json
import requests
import pandas
import sys


def run(event, context):
    print(os.environ['S3_BUCKET'])
    print(os.environ['S3_KEY_BASE'])
    url = "https://cache1.phantombooster.com/ukZxdjCQmz0/Vg7zuvUGSEG6yzglJ6jkhA/result.json"
    request = requests.get(url)
    list_of_dicts_data = request.json()
    print(len(list_of_dicts_data))