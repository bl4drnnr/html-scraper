from lxml import html
import requests
import sys


ALLOWED_FLAGS = ['--help', '-h', '-u', '--url']


def print_help():
    print('Documentation.')
    print('-h, --help\tPrint documentation manual.')
    print('-u, --url\tPass URL of page of page to scrap. Example: -u https://example.com or --url=https://example.com')


def print_flags_error():
    print('\nWrong flag!')
    print('Please, check documentation (-h, --help) in order to check all available flags.')
    exit()


def print_input():
    print('****************************************************************************')
    print(' _   _ ________  ___ _          _____ _____ ______  ___  ______ ___________ ')
    print('| | | |_   _|  \/  || |        /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \\')
    print('| |_| | | | | .  . || |  ______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /')
    print('|  _  | | | | |\/| || | |______|`--. \ |    |    /|  _  ||  __/|  __||    / ')
    print('| | | | | | | |  | || |____    /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ ')
    print('\_| |_/ \_/ \_|  |_/\_____/    \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|')
    print('****************************************************************************')

    print('Welcome, username, you here to scrap some HTML, right? Well, I knew that, so, let\'s start then!')
    print('Let\'s start with simple configuration of what you exactly want.\n')


def print_format_request():
    print('\nAnd the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')
    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------\n')


def set_pagination(url):
    is_pagination = input('Is there any pagination in case if you want to get data from a couple of pages, not only one? [Y/N]: ')
    provided_pagination = ''

    if is_pagination == 'Y' or is_pagination == 'y':
        quantity_of_pages = input('\nWell, what about quantity of pages?: ')

        try:
            int(quantity_of_pages)
        except (Exception,):
            print('Nah... Doesn\'t seem to be number...')

        pagination_already_provided = input('Were pagination already provided in URL params or as route? [Y/N]: ')

        if pagination_already_provided == 'Y' or pagination_already_provided == 'y':
            url_param_or_route = input('Is it URL param (example: https://example.com?page=4) or part or route (example: https://example.com/4/)? (1/2): ')
            if url_param_or_route == '1':
                provided_pagination = input('Provide pagination\'s key and value in the same way (and same value) as you did it providing it as param, for example - page=4: ')
                if provided_pagination not in url:
                    print('\nWell... Probably you provided something wrong...')
                    exit()
            elif url_param_or_route == '2':
                provided_pagination = input('Set the place of this pagination (example for https://example.com/4/, you would provide /4/): ')
                if len(provided_pagination) != 3 or provided_pagination[0] != '/' or provided_pagination[-1] != '/' or provided_pagination[1] not in '0123456789':
                    print('\nWrong format! Please, try again!')
                    exit()
            else:
                print('\nNah... Doesn\'t seem to be right answer...')
                exit()
        else:
            print('\nWell, then you should provide it in URL route.')
            print('It could be URL param (example: https://example.com?page=4) or part or route (example: https://example.com/4/)')
            exit()

    return provided_pagination


def single_request(url, cookies, headers, tag_to_extract):
    try:
        print('Sending request to {}'.format(url))
        page = requests.get(url, cookies=cookies, headers=headers)
        tree = html.fromstring(page.content)
        return tree.xpath('//{}/text()'.format(tag_to_extract))
    except Exception as e:
        raise Exception(e)


def request_with_pagination(url, cookies, headers, tag_to_extract, pagination):
    try:
        print('Sending request to {}'.format(url))
        if '=' in pagination:
            pass
        elif pagination[0] == '/':
            pass
        else:
            print('\nSomething went wrong with pagination!')
            exit()
        page = requests.get(url, cookies=cookies, headers=headers)
        tree = html.fromstring(page.content)
        return tree.xpath('//{}/text()'.format(tag_to_extract))
    except Exception as e:
        raise Exception(e)


def set_option_type(option_type):
    return {
        'headers': {
            'set': 'Wanna set headers? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': '\nWhat about quantity of headers? (Integer number only): ',
            'format': 'Provide header in next format - key=value'
        },
        'cookies': {
            'set': 'Wanna send with some cookie? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': '\nWhat about quantity of cookies? (Integer number only): ',
            'format': 'Provide cookie in next format - key=value'
        },
        'params': {
            'set': 'Are there any URL params you want to provide (if you haven\'t done it in URL yet) [Y/N]: ',
            'quantity': '\nWhat about quantity of params? (Integer number only): ',
            'format': 'Now, provide URL params in the next format - key=value.'
        }
    }[option_type]


def set_option(option, url=''):
    values = {}
    texts = set_option_type(option)
    set_option_choose = input(texts['set'])

    if set_option_choose == 'Y' or set_option_choose == 'y':
        quantity_option = texts['quantity']
        quantity = input(quantity_option)
        print()

        try:
            int(quantity)
        except (Exception,):
            print('Nah... Doesn\'t seem to be number...')

        items = []
        print(texts['format'])
        for i in range(0, int(quantity)):
            provided_value = input('Key and value: ')

            if '=' not in provided_value or provided_value[0] == '=' or provided_value[-1] == '':
                print('\nWrong')
                exit()

            items.append(provided_value)

        if option != 'params':
            if len(items) > 0:

                for value in items:
                    values[value.split('=')[0]] = value.split('=')[1]
        else:
            if url[-1] == '/':
                url = url[:-1]

            for i, param in enumerate(items):
                if i == 0:
                    url += '?{}={}'.format(param.split('=')[0], param.split('=')[1])
                else:
                    url += '&{}={}'.format(param.split('=')[0], param.split('=')[1])

            return url

    if option == 'params':
        return url
    else:
        return values


def main():
    print_input()
    url = input('First of all, provide me with url of page to scrap: ')

    if url[0:7] != 'http://' and url[0:8] != 'https://':
        print('\nURL must start with http:// or https:// !')
        exit()

    print('\nOkay, here we go with options!')

    updated_url = set_option('params', url)
    cookies = set_option('cookies')
    headers = set_option('headers')
    pagination = set_pagination(url)

    print_format_request()

    tag_to_extract = input('So, what about tag to extract?: ')

    print('\nAnd... That\'s it! Here we go!')

    content = request_with_pagination(updated_url, cookies, headers, tag_to_extract, pagination) if len(pagination) > 0 else single_request(updated_url, cookies, headers, tag_to_extract)

    print('\nOf... Seems like everything went right. Let\'s end up with this.')

    remove_whitespaces = input('Wanna remove all whitespace signs? [Y/N]: ')
    if remove_whitespaces == 'Y' or remove_whitespaces == 'y':
        updated_content = []
        for item in content:
            updated_content.append(item.strip())
        content = updated_content

    save_to_file = input('Save result to file? [Y/N]: ')
    if save_to_file == 'Y' or save_to_file == 'y':
        try:
            file_name = input('Please, provide file name: ')
            final_content = ''

            f = open(f'{file_name}.txt', 'w')

            for item in content:
                final_content += f'{item},'

            f.write(final_content)
            f.close()

            print('And... Done!')
        except (Exception,):
            print('Oops... Something went wrong! Please, check file name.')
    else:
        print('\n---------------------')
        print('Result:', content)
        print('---------------------\n')


if __name__ == '__main__':
    main()
