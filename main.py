from lxml import html
import requests


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

    options = {
        'params': [],
        'cookies': {},
        'headers': {}
    }

    url = input('First of all, provide me with url of page to scrap: ')
    options['url'] = url
    print('\nOkay, here we go with options!')

    anyParams = input('\nAre there any URL params you want to provide (if you haven\'t done it in URL yet) [Y/N]: ')

    if anyParams == 'Y' or anyParams == 'y':
        quantityOfParams = input('What about quantity of params? (Integer number only): ')
        print()

        try:
            int(quantityOfParams)
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        print('Now, provide URL params in the next format - key=value.')
        for i in range(0, int(quantityOfParams)):
            providedParam = input('Key and value of URL param: ')

            if '=' not in providedParam or providedParam[0] == '=' or providedParam[-1] == '':
                print('Wrong param format!')
                exit()

            options['params'].append(providedParam)

        if url[-1] == '/':
            url = url[:-1]

        for param, i in options['params']:
            if i == 0:
                url += '?{}={}'.format(param.split('=')[0], param.split('=')[1])
            else:
                url += '&{}={}'.format(param.split('=')[0], param.split('=')[1])

        options['url'] = url
        # Todo - Ask user for pagination

    anyCookie = input('Wanna send with some cookie? (for example, if access to page is restricted by authentication) [Y/N]: ')
    if anyCookie == 'Y' or anyCookie == 'y':
        quantityOfCookies = input('What about quantity of cookies? (Integer number only): ')
        print()

        try:
            int(quantityOfCookies)
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        cookies = []
        print('Provide cookie in next format - key=value')
        for i in range(0, int(quantityOfCookies)):
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

    anyHeaders = input('Wanna set headers? (for example, if access to page is restricted by authentication) [Y/N]: ')
    if anyHeaders == 'Y' or anyHeaders == 'y':
        quantityOfHeaders = input('What about quantity of headers? (Integer number only): ')
        print()

        try:
            int(quantityOfHeaders)
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        headers = []
        print('Provide header in next format - key=value')
        for i in range(0, int(quantityOfHeaders)):
            providedHeader = input('Key and value of header: ')

            if '=' not in providedHeader or providedHeader[0] == '=' or providedHeader[-1] == '':
                print('Wrong cookie format!')
                exit()

            headers.append(providedHeader)

        if len(headers) > 0:
            headerObject = {}

            for header in headers:
                headerObject[header.split('=')[0]] = header.split('=')[1]

            options['headers'] = headerObject

    print('\nAnd the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')
    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------\n')

    tagToExtract = input('So, what about tag to extract?: ')

    print('\nAnd... That\'s it! Here we go!')

    try:
        print('Sending request to {}'.format(options['url']))
        page = requests.get(url, cookies=options['cookies'], headers=options['headers'])
        tree = html.fromstring(page.content)
        content = tree.xpath('//{}/text()'.format(tagToExtract))
    except Exception as e:
        raise Exception(e)

    print('\nOf... Seems like everything went right. Let\'s end up with this.')

    removeWhitespaces = input('Wanna remove all whitespace signs? [Y/N]: ')
    if removeWhitespaces == 'Y' or removeWhitespaces == 'y':
        for item in content:
            item.strip()

    saveToFile = input('Save result to file? [Y/N]: ')
    if saveToFile == 'Y' or saveToFile == 'y':
        pass
        # Todo - Ask user for write result to file
    else:
        print('\n---------------------')
        print('Result:', content)
        print('---------------------\n')


if __name__ == '__main__':
    main()
