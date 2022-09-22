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
        'params': []
    }

    url = input('First of all, provide me with url of page to scrap: ')
    print()
    print('Okay, here we go with options!')

    anyParams = input('Are there any url params you want to provide (if you haven\'t done it in URL) [Y/N]: ')

    if anyParams == 'Y' or anyParams == 'y':
        options['quantityOfParams'] = input('What about quantity of params? (Integer number only): ')
        print()

        try:
            int(options['quantityOfParams'])
        except (Exception,):
            print('Nah... Doe\'s seem to be number...')

        print('Now, provide URL params in this format - key=value.')
        for i in range(0, int(options['quantityOfParams'])):
            providedParam = input('Key and value of URL param: ')

            if '=' not in providedParam or providedParam[0] == '=' or providedParam[-1] == '':
                print('Wrong param format!')
                exit()

            options['params'].append(providedParam)

    print(options)


if __name__ == '__main__':
    main()
