import json

import requests
import threading


def check_url(url):
    result_list = {}
    try:
        status_url = requests.get(url)
        print("Target: ", url)
        print("Status: ", status_url.ok, '\n')
        result_list['url'] = url
        result_list['is_ok'] = status_url.ok
        result_list['status_code'] = status_url.status_code

    except requests.exceptions.ConnectionError:
        status_url = False
        print("Target: ", url)
        print("Status: ", status_url, '\n')
        result_list['url'] = url
        result_list['is_ok'] = status_url
        result_list['status_code'] = 'null'

    final_result.append(result_list)


if __name__ == '__main__':
    links_list = []
    final_result = []
    with open('links.txt', 'r') as links:
        for item in links:
            links_list.append(item.replace('\n', ''))

    for item in links_list:
        t = threading.Thread(target=check_url(item))
        t.start()

json_object = json.dumps(final_result, indent=2)

with open('result_links.json', "w") as json_file:
    json_file.write(json_object)