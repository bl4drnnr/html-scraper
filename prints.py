from termcolor import colored


def print_input():
    print(colored('****************************************************************************', 'green'))
    print(colored(' _   _ ________  ___ _          _____ _____ ______  ___  ______ ___________ ', 'green'))
    print(colored('| | | |_   _|  \/  || |        /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \\', 'green'))
    print(colored('| |_| | | | | .  . || |  ______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /', 'green'))
    print(colored('|  _  | | | | |\/| || | |______|`--. \ |    |    /|  _  ||  __/|  __||    / ', 'green'))
    print(colored('| | | | | | | |  | || |____    /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ ', 'green'))
    print(colored('\_| |_/ \_/ \_|  |_/\_____/    \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|', 'green'))
    print(colored('****************************************************************************', 'green'))

    print(colored('Welcome, username, you here to scrap some HTML, right? Well, I knew that, so, let\'s start then!', 'white', attrs=['reverse']))
    print(colored('Let\'s start with simple configuration of what you exactly want.\n', 'white', attrs=['reverse']))


def print_format_request():
    print('\nAnd the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')
    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------\n')


def print_help():
    print('Documentation.')
    print('-h, --help\t\tPrint documentation manual.')
    print('-u, --url\t\tPass URL of page of page to scrap. Example: -u https://example.com or --url=https://example.com')
    print('-o, --output\t\tWrite result in file. Example: -u output.txt or --output=output.txt')
    exit()


def print_flags_error():
    print(colored('Wrong flag!', 'red', attrs=['reverse']))
    print(colored('Please, check documentation (-h, --help) in order to check all available flags.', 'red', attrs=['reverse']))
    exit(2)


def only_one_flag_allowed():
    print(colored('Only one flag is allowed!', 'red', attrs=['reverse']))
    print(colored('Please, check documentation (-h, --help) in order to check all available flags.', 'red', attrs=['reverse']))
    exit(2)
