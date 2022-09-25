from lxml import html
from termcolor import colored

import requests


def single_request(url, cookies, headers, tag_to_extract):
    try:
        print(colored('Sending request to {}'.format(url), 'blue'))
        page = requests.get(url, cookies=cookies, headers=headers)
        tree = html.fromstring(page.content)
        return tree.xpath('//{}/text()'.format(tag_to_extract))
    except Exception as e:
        raise Exception(e)


def request_with_pagination(url, cookies, headers, tag_to_extract, pagination):
    result = []
    try:
        split_url = url.split(pagination['provided_pagination'])
        for i in range(1, pagination['quantity_of_pages'] + 1):
            if '=' in pagination['provided_pagination']:
                updated_url = split_url[0] + pagination['provided_pagination'].split('=')[0] + '=' + str(i) + split_url[1]
            else:
                updated_url = split_url[0] + f'/{str(i)}/' + split_url[1]
            print(colored('Sending request to {}'.format(updated_url), 'blue'))
            page = requests.get(updated_url, cookies=cookies, headers=headers)
            tree = html.fromstring(page.content)
            tree_content = tree.xpath('//{}/text()'.format(tag_to_extract))

            for item in tree_content:
                result.append(item)
    except Exception as e:
        raise Exception(e)

    return result
