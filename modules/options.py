from termcolor import colored


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
            print(colored('Nah... Doesn\'t seem to be number...', 'red', attrs=['reverse']))

        items = []
        print(texts['format'])
        for i in range(0, int(quantity)):
            provided_value = input('Key and value: ')

            if '=' not in provided_value or provided_value[0] == '=' or provided_value[-1] == '':
                print(colored('\nWrong format', 'red', attrs=['reverse']))
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
