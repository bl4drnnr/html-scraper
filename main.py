from lxml import html
import requests


def main():
    print('****************************************************************************')
    print(' _   _ ________  ___ _          _____ _____ ______  ___  ______ ___________ ')
    print('| | | |_   _|  \/  || |        /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \\')
    print('| |_| | | | | .  . || |  ______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /')
    print('|  _  | | | | |\/| || | |______|`--. \ |    |    /|  _  ||  __/|  __||    / ')
    print('| | | | | | | |  | || |____    /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ ')
    print('\_| |_/ \_/ \_|  |_/\_____/    \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|')
    print('****************************************************************************')

    print('Welcome, username, you here to scrap some HTML, right? Well, I knew that, so, let\'s start then!')
    print('Let\'s start with simple configuration of what you exactly want.')
    print()

    options = {
        'params': [],
        'cookies': {},
        'headers': {}
    }

    url = input('First of all, provide me with url of page to scrap: ')
    print()
    print('Okay, here we go with options!')

    anyParams = input('Are there any URL params you want to provide (if you haven\'t done it in URL yet) [Y/N]: ')

    if anyParams == 'Y' or anyParams == 'y':
        options['quantityOfParams'] = input('What about quantity of params? (Integer number only): ')
        print()

        try:
            int(options['quantityOfParams'])
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        print('Now, provide URL params in the next format - key=value.')
        for i in range(0, int(options['quantityOfParams'])):
            providedParam = input('Key and value of URL param: ')

            if '=' not in providedParam or providedParam[0] == '=' or providedParam[-1] == '':
                print('Wrong param format!')
                exit()

            options['params'].append(providedParam)

    print()

    anyCookie = input('Wanna send with some cookie? (for example, if access to page is restricted by authentication) [Y/N]: ')
    if anyCookie == 'Y' or anyCookie == 'y':
        options['quantityOfCookies'] = input('What about quantity of cookies? (Integer number only): ')
        print()

        try:
            int(options['quantityOfCookies'])
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        cookies = []
        print('Provide cookie in next format - key=value')
        for i in range(0, int(options['quantityOfCookies'])):
            providedCookie = input('Key and value of cookie: ')

            if '=' not in providedCookie or providedCookie[0] == '=' or providedCookie[-1] == '':
                print('Wrong cookie format!')
                exit()

            cookies.append(providedCookie)

        if len(cookies) > 0:
            cookieObject = {}

            for cookie in cookies:
                cookieObject[cookie.split('=')[0]] = cookie.split('=')[1]

            options['cookies'] = cookieObject

    print()

    print('And the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')

    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------')
    print()

    tagToExtract = input('So, what about tag to extract?: ')
    print()

    print('And... That\'s it! Here we go!')

    page = requests.get(url, cookies=options['cookies'], headers=options['headers'])
    tree = html.fromstring(page.content)

    try:
        content = tree.xpath('//{}/text()'.format(tagToExtract))
    except Exception as e:
        raise Exception(e)

    print(content)


if __name__ == '__main__':
    main()
