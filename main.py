import os.path

from lxml import html
import requests


def set_option_type(option_type):
    return {
        'headers': {
            'set': 'Wanna set headers? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': 'What about quantity of headers? (Integer number only): ',
            'format': 'Provide header in next format - key=value'
        },
        'cookies': {
            'set': 'Wanna send with some cookie? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': 'What about quantity of cookies? (Integer number only): ',
            'format': 'Provide cookie in next format - key=value'
        },
        'params': {
            'set': '\nAre there any URL params you want to provide (if you haven\'t done it in URL yet) [Y/N]: ',
            'quantity': 'What about quantity of params? (Integer number only): ',
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
            print('Nah... Doe\'s seem to be number...')

        items = []
        print(texts['format'])
        for i in range(0, int(quantity)):
            provided_value = input('Key and value: ')

            if '=' not in provided_value or provided_value[0] == '=' or provided_value[-1] == '':
                print('Wrong')
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
    # Todo - Format text with styles
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

    url = input('First of all, provide me with url of page to scrap: ')

    if url[0:7] != 'http://' and url[0:8] != 'https://':
        print('URL must start with http:// or https:// !')
        exit()

    print('\nOkay, here we go with options!')

    # Todo - Ask user for pagination

    updated_url = set_option('params', url)
    cookies = set_option('cookies')
    headers = set_option('headers')

    print('\nAnd the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')
    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------\n')

    tag_to_extract = input('So, what about tag to extract?: ')

    print('\nAnd... That\'s it! Here we go!')

    try:
        print('Sending request to {}'.format(updated_url))
        page = requests.get(updated_url, cookies=cookies, headers=headers)
        tree = html.fromstring(page.content)
        content = tree.xpath('//{}/text()'.format(tag_to_extract))
    except Exception as e:
        raise Exception(e)

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
